# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.


class Schedule(object):

    def __init__(self, params=None):
        if params is None:
            self.__schedule_id = None
            self.__owner_id = None
            self.__name = None
            self.__description = None
            self.__create_at = None
            self.__update_at = None
        else:
            self.set_schedule_id(params['scheduleId'] if 'scheduleId' in params.keys() else None)
            self.set_owner_id(params['ownerId'] if 'ownerId' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_description(params['description'] if 'description' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)

    def get_schedule_id(self):
        """
        スケジュールGRNを取得
        :return: スケジュールGRN
        :rtype: unicode
        """
        return self.__schedule_id

    def set_schedule_id(self, schedule_id):
        """
        スケジュールGRNを設定
        :param schedule_id: スケジュールGRN
        :type schedule_id: unicode
        """
        self.__schedule_id = schedule_id

    def get_owner_id(self):
        """
        オーナーIDを取得
        :return: オーナーID
        :rtype: unicode
        """
        return self.__owner_id

    def set_owner_id(self, owner_id):
        """
        オーナーIDを設定
        :param owner_id: オーナーID
        :type owner_id: unicode
        """
        self.__owner_id = owner_id

    def get_name(self):
        """
        スケジュール名を取得
        :return: スケジュール名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        スケジュール名を設定
        :param name: スケジュール名
        :type name: unicode
        """
        self.__name = name

    def get_description(self):
        """
        説明文を取得
        :return: 説明文
        :rtype: unicode
        """
        return self.__description

    def set_description(self, description):
        """
        説明文を設定
        :param description: 説明文
        :type description: unicode
        """
        self.__description = description

    def get_create_at(self):
        """
        作成日時(エポック秒)を取得
        :return: 作成日時(エポック秒)
        :rtype: int
        """
        return self.__create_at

    def set_create_at(self, create_at):
        """
        作成日時(エポック秒)を設定
        :param create_at: 作成日時(エポック秒)
        :type create_at: int
        """
        self.__create_at = create_at

    def get_update_at(self):
        """
        最終更新日時(エポック秒)を取得
        :return: 最終更新日時(エポック秒)
        :rtype: int
        """
        return self.__update_at

    def set_update_at(self, update_at):
        """
        最終更新日時(エポック秒)を設定
        :param update_at: 最終更新日時(エポック秒)
        :type update_at: int
        """
        self.__update_at = update_at

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(Schedule, self).__getitem__(key)

    def to_dict(self):
        return {
            "scheduleId": self.__schedule_id,
            "ownerId": self.__owner_id,
            "name": self.__name,
            "description": self.__description,
            "createAt": self.__create_at,
            "updateAt": self.__update_at,
        }
