#!/usr/bin/env python3
#
# Copyright 2018 Nicholas de Jong  <contact[at]nicholasdejong.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os, sys, json
import bcrypt  # pip install bcrypt
from dotenv import load_dotenv

try:
    from PfsenseFauxapi.PfsenseFauxapi import PfsenseFauxapi
except:
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from PfsenseFauxapi.PfsenseFauxapi import PfsenseFauxapi

load_dotenv()

# config
fauxapi_host=os.getenv("HOST_IP")
fauxapi_apikey=os.getenv("API_KEY")
fauxapi_apisecret=os.getenv("API_SECRET")


class UserGroupManagementFauxapiException(Exception):
    pass


class UserGroupManagementFauxapi():

    fauxapi_host = None
    fauxapi_apikey = None
    fauxapi_apisecret = None

    system_config= None

    FauxapiLib = None

    def __init__(self, fauxapi_host, fauxapi_apikey, fauxapi_apisecret, debug=False):
        self.FauxapiLib = PfsenseFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret, debug)

    # user functions
    # =========================================================================

    def get_users(self):
        self._reload_system_config()

        response_data = {}
        for user in self.system_config['system']['user']:
            response_data[user['name']] = user
            del(response_data[user['name']]['name'])
        return response_data

    def add_user(self, username):
        self._reload_system_config()

        user_index, user = self._get_entity('user', username)
        if user_index is not None:
            raise UserGroupManagementFauxapiException('user already exists', username)

        user = {
            'scope': 'user',
            'bcrypt-hash': 'no-password-set',
            'descr': '',
            'name': username,
            'expires': '',
            'dashboardcolumns': '2',
            'authorizedkeys': '',
            'ipsecpsk': '',
            'webguicss': 'pfSense.css',
            'uid': self._get_next_id('uid'),
        }

        patch_system_user = {
            'system': {
                'user': self.system_config['system']['user']
            }
        }
        patch_system_user['system']['user'].append(user)

        response = self.FauxapiLib.config_patch(patch_system_user)
        if response['message'] != 'ok':
            raise UserGroupManagementFauxapiException('unable to add user', response['message'])

        self._increment_next_id('uid')

        return user

    def manage_user(self, username, attributes):
        self._reload_system_config()

        valid_attributes = ['password','descr','expires','dashboardcolumns','authorizedkeys','ipsecpsk','webguicss','disabled','priv']

        user_index, user = self._get_entity('user', username)
        if user_index is None:
            raise UserGroupManagementFauxapiException('user does not exist', username)

        if type(attributes) != dict:
            raise UserGroupManagementFauxapiException('attributes is incorrect type')

        for attribute, value in attributes.items():
            if attribute not in valid_attributes:
                raise UserGroupManagementFauxapiException('unsupported attribute type', attribute)

            if attribute == 'disabled':
                if value is True:
                    user[attribute] = ''
                else:
                    if attribute in user:
                        del(user[attribute])
            elif attribute == 'password':
                user['bcrypt-hash'] = bcrypt.hashpw(value.encode('utf8'), bcrypt.gensalt()).decode('utf8')
            else:
                if len(value) == 0 and attribute in user:
                    del(user[attribute])
                elif len(value) > 0:
                    user[attribute] = value

        patch_system_user = {
            'system': {
                'user': self.system_config['system']['user']
            }
        }
        patch_system_user['system']['user'][user_index] = user

        response = self.FauxapiLib.config_patch(patch_system_user)
        if response['message'] != 'ok':
            raise UserGroupManagementFauxapiException('unable to manage user', response['message'])

        return user

    def remove_user(self, username):
        self._reload_system_config()

        user_index, user = self._get_entity('user', username)
        if user_index is None:
            raise UserGroupManagementFauxapiException('user does not exist', username)

        patch_system_user = {
            'system': {
                'user': self.system_config['system']['user']
            }
        }
        del(patch_system_user['system']['user'][user_index])

        response = self.FauxapiLib.config_patch(patch_system_user)
        if response['message'] != 'ok':
            raise UserGroupManagementFauxapiException('unable to remove user', response['message'])

        return user

    # openvpn functions
    # =========================================================================

    def get_ovpn_users(self):
        self._reload_system_config()

        response_data = {}
        for user in self.system_config['openvpn']['openvpn-csc']:
            response_data[user['common_name']] = user
            del(response_data[user['common_name']]['common_name'])
        return response_data

    def add_ovpn_csc(self, username, ip, subnet):
        self._reload_system_config()

        user_index, user = self._get_entity('user', username)
        if user_index is None:
            raise UserGroupManagementFauxapiException('user does not exist', username)

        user_index, user = self._get_csc('openvpn-csc', username)
        if user_index is not None:
            raise UserGroupManagementFauxapiException('user already has static ip binding', username)

        command = "ifconfig-push " + ip + " " + subnet + ";"

        user = {
            'server_list': '',
            'custom_options': command,
            'common_name': username,
            'block': '',
            'description': '',
            'tunnel_network': '',
            'tunnel_networkv6': '',
            'local_network': '',
            'local_networkv6': '',
            'remote_network': '',
            'remote_networkv6': '',
            'gwredir': '',
            'push_reset': '',
            'netbios_enable': '',
            'netbios_ntype': '0',
            'netbios_scope': '',
        }

        patch_openvpn_csc = {
            'openvpn': {
                'openvpn-csc': self.system_config['openvpn']['openvpn-csc']
            }
        }
        patch_openvpn_csc['openvpn']['openvpn-csc'].append(user)

        response = self.FauxapiLib.config_patch(patch_openvpn_csc)
        if response['message'] != 'ok':
            raise UserGroupManagementFauxapiException('unable to add openvpn user csc', response['message'])

        return user

    def remove_ovpn_csc(self, username):
        self._reload_system_config()

        user_index, user = self._get_csc('openvpn-csc', username)
        if user_index is None:
            raise UserGroupManagementFauxapiException('user does not exist', username)

        patch_openvpn_csc = {
            'openvpn': {
                'openvpn-csc': self.system_config['openvpn']['openvpn-csc']
            }
        }
        del(patch_openvpn_csc['openvpn']['openvpn-csc'][user_index])

        response = self.FauxapiLib.config_patch(patch_openvpn_csc)
        if response['message'] != 'ok':
            raise UserGroupManagementFauxapiException('unable to remove user', response['message'])

        return user

    # squidguard functions
    # =========================================================================

    def get_sg_category(self):
        self._reload_system_config()

        response_data = {}
        for cat in self.system_config['installedpackages']['squidguarddest']['config']:
            response_data[cat['name']] = cat
            del(response_data[cat['name']]['name'])
        return response_data

    def get_sg_groupacl(self):
        self._reload_system_config()

        response_data = {}
        for cat in self.system_config['installedpackages']['squidguardacl']['config']:
            response_data[cat['name']] = cat
            del(response_data[cat['name']]['name'])
        return response_data

    def add_sg_category(self, cat_name, domain_list):
        self._reload_system_config()

        cat_index, cat = self._get_entity_3('installedpackages', 'squidguarddest', 'config', 'name', cat_name)
        if cat_index is not None:
            raise UserGroupManagementFauxapiException('category already exists', cat)

        user = {
            'name': cat_name,
            'domains': domain_list,
            'urls': '',
            'expressions': '',
            'redirect_mode': 'rmod_none',
            'redirect': '',
            'description': '',
            'enablelog': 'on',
        }

        patch_sg_category = {
            'installedpackages': {
                'squidguarddest': {
                    'config': self.system_config['installedpackages']['squidguarddest']['config']
                }
            }
        }

        patch_sg_category['installedpackages']['squidguarddest']['config'].append(user)

        response = self.FauxapiLib.config_patch(patch_sg_category)
        if response['message'] != 'ok':
            raise UserGroupManagementFauxapiException('unable to add squidguard category', response['message'])

        return user

    def add_sg_groupacl(self, gacl_name, source_ip):
        self._reload_system_config()

        gacl_index, gacl = self._get_entity_3('installedpackages', 'squidguardacl', 'config', 'name', gacl_name)
        if gacl_index is not None:
            raise UserGroupManagementFauxapiException('group acl already exists', gacl)

        gacl_index, gacl = self._get_entity_3('installedpackages', 'squidguardacl', 'config', 'source', source_ip)
        if gacl_index is not None:
            raise UserGroupManagementFauxapiException('source ip already exists', gacl)

        user = {
            'disabled': '',
            'name': gacl_name,
            'source': source_ip,
            'time': '',
            'dest': 'global_whitelist !test_blacklist2 all [ all]',
            'notallowingip': 'on',
            'redirect_mode': 'rmod_none',
            'redirect': '',
            'safesearch': '',
            'rewrite': '',
            'overrewrite': '',
            'description': '',
            'enablelog': 'on',
        }

        patch_sg_groupacl = {
            'installedpackages': {
                'squidguardacl': {
                    'config': self.system_config['installedpackages']['squidguardacl']['config']
                }
            }
        }

        patch_sg_groupacl['installedpackages']['squidguardacl']['config'].append(user)

        response = self.FauxapiLib.config_patch(patch_sg_groupacl)
        if response['message'] != 'ok':
            raise UserGroupManagementFauxapiException('unable to add squidguard group acl', response['message'])

        return user

    def remove_sg_category(self, cat_name):
        self._reload_system_config()

        cat_index, cat = self._get_entity_3('installedpackages', 'squidguarddest', 'config', 'name', cat_name)
        if cat_index is None:
            raise UserGroupManagementFauxapiException('category does not exist', cat)

        patch_sg_category = {
            'installedpackages': {
                'squidguarddest': {
                    'config': self.system_config['installedpackages']['squidguarddest']['config']
                }
            }
        }
        del(patch_sg_category['installedpackages']['squidguarddest']['config'][cat_index])

        response = self.FauxapiLib.config_patch(patch_sg_category)
        if response['message'] != 'ok':
            raise UserGroupManagementFauxapiException('unable to remove category', response['message'])

        return cat

    def remove_sg_groupacl(self, gacl_name):
        self._reload_system_config()

        gacl_index, gacl = self._get_entity_3('installedpackages', 'squidguardacl', 'config', 'name', gacl_name)
        if gacl_index is None:
            raise UserGroupManagementFauxapiException('group acl does not exist', gacl)

        patch_sg_groupacl = {
            'installedpackages': {
                'squidguardacl': {
                    'config': self.system_config['installedpackages']['squidguardacl']['config']
                }
            }
        }
        del(patch_sg_groupacl['installedpackages']['squidguardacl']['config'][gacl_index])

        response = self.FauxapiLib.config_patch(patch_sg_groupacl)
        if response['message'] != 'ok':
            raise UserGroupManagementFauxapiException('unable to remove category', response['message'])

        return gacl

    # group functions
    # =========================================================================

    def get_groups(self):
        self._reload_system_config()

        response_data = {}
        for group in self.system_config['system']['group']:
            response_data[group['name']] = group
            del(response_data[group['name']]['name'])
        return response_data

    def add_group(self, groupname):
        self._reload_system_config()

        group_index, group = self._get_entity('group', groupname)
        if group_index is not None:
            raise UserGroupManagementFauxapiException('group already exists', groupname)

        group = {
            'scope': 'local',
            'description': '',
            'name': groupname,
            'gid': self._get_next_id('gid'),
        }

        patch_system_group = {
            'system': {
                'group': self.system_config['system']['group']
            }
        }
        patch_system_group['system']['group'].append(group)

        response = self.FauxapiLib.config_patch(patch_system_group)
        if response['message'] != 'ok':
            raise UserGroupManagementFauxapiException('unable to add group', response['message'])

        self._increment_next_id('gid')

        return group

    def manage_group(self, groupname, attributes):
        self._reload_system_config()

        valid_attributes = ['description','member','priv']

        group_index, group = self._get_entity('group', groupname)
        if group_index is None:
            raise UserGroupManagementFauxapiException('group does not exist', groupname)

        if type(attributes) != dict:
            raise UserGroupManagementFauxapiException('attributes is incorrect type')

        for attribute, value in attributes.items():
            if attribute not in valid_attributes:
                raise UserGroupManagementFauxapiException('unsupported attribute type', attribute)

            if attribute == 'member':
                if type(value) != list:
                    raise UserGroupManagementFauxapiException('member attribute is incorrect type')
            elif attribute == 'priv':
                if type(value) != list:
                    raise UserGroupManagementFauxapiException('priv attribute is incorrect type')

            if len(value) == 0 and attribute in group:
                del(group[attribute])
            elif len(value) > 0:
                group[attribute] = value

        patch_system_group = {
            'system': {
                'group': self.system_config['system']['group']
            }
        }
        patch_system_group['system']['group'][group_index] = group

        response = self.FauxapiLib.config_patch(patch_system_group)
        if response['message'] != 'ok':
            raise UserGroupManagementFauxapiException('unable to manage group', response['message'])

        return group

    def remove_group(self, groupname):
        self._reload_system_config()

        group_index, group = self._get_entity('group', groupname)
        if group_index is None:
            raise UserGroupManagementFauxapiException('group does not exist', groupname)

        patch_system_group = {
            'system': {
                'group': self.system_config['system']['group']
            }
        }
        del(patch_system_group['system']['group'][group_index])

        response = self.FauxapiLib.config_patch(patch_system_group)
        if response['message'] != 'ok':
            raise UserGroupManagementFauxapiException('unable to remove group', response['message'])

        return group

    # internal helper functions
    # =========================================================================

    def _get_entity(self, entity_type, entity_name):

        entity = None
        entity_index = 0
        for entity_data in self.system_config['system'][entity_type]:
            if entity_data['name'] == entity_name:
                entity = entity_data
                break
            entity_index += 1

        if entity is None:
            return None, None

        return entity_index, entity

    def _get_csc(self, entity_type, entity_name):

        entity = None
        entity_index = 0
        for entity_data in self.system_config['openvpn'][entity_type]:
            if entity_data['common_name'] == entity_name:
                entity = entity_data
                break
            entity_index += 1

        if entity is None:
            return None, None

        return entity_index, entity

    def _get_entity_3(self, entity_l1, entity_l2, entity_l3, entity_label, entity_name):

        entity = None
        entity_index = 0
        for entity_data in self.system_config[entity_l1][entity_l2][entity_l3]:
            if entity_data[entity_label] == entity_name:
                entity = entity_data
                break
            entity_index += 1

        if entity is None:
            return None, None

        return entity_index, entity

    def _get_next_id(self, id_type):
        id_name = 'next{}'.format(id_type)
        return self.system_config['system'][id_name]

    def _increment_next_id(self, id_type):
        id_name = 'next{}'.format(id_type)
        next_id = int(self._get_next_id(id_type)) + 1
        patch_system_nextid = {
            'system': {
                id_name: str(next_id)
            }
        }
        response = self.FauxapiLib.config_patch(patch_system_nextid)
        if response['message'] != 'ok':
            raise UserGroupManagementFauxapiException('unable to increment the nextid', id_type)
        return next_id

    def _reload_system_config(self):
        self.system_config = self.FauxapiLib.config_get()


if __name__ == '__main__':

    UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)

    # get_users
    users = UGMF.get_users()
    print(json.dumps(users))

    # get_groups
    groups = UGMF.get_groups()
    print(json.dumps(groups))

    # =========================================================================

    # add_user
    user = UGMF.add_user('someuser')
    print(json.dumps(user))

    # manage_user attributes
    attributes = {
        'disabled': False,
        'descr': 'some new name',
        'password': 'awesomepassword',
        'expires': '12/25/2020',
        'authorizedkeys': 'insert-ssh-key-material-here',
        'priv': ['page-all'],
    }
    user = UGMF.manage_user('someuser', attributes)
    print(json.dumps(user))

    # =========================================================================

    # add_group
    group = UGMF.add_group('somegroup')
    print(json.dumps(group))

    # manage_group attributes
    attributes = {
        'description': 'some new group name',
        'member': [user['uid']],
        'priv': ['page-all'],
    }
    group = UGMF.manage_group('somegroup', attributes)
    print(json.dumps(group))

    # =========================================================================

    # remove_group
    group = UGMF.remove_group('somegroup')
    print(json.dumps(group))

    # remove_user
    user = UGMF.remove_user('someuser')
    print(json.dumps(user))