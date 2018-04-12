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


class Trigger(object):

    def __init__(self, params=None):
        if params is None:
            self.__user_id = None
            self.__trigger_name = None
            self.__trigger_at = None
        else:
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
            self.set_trigger_name(params['triggerName'] if 'triggerName' in params.keys() else None)
            self.set_trigger_at(params['triggerAt'] if 'triggerAt' in params.keys() else None)

    def get_user_id(self):
        """
        ユーザIDを取得
        :return: ユーザID
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        ユーザIDを設定
        :param user_id: ユーザID
        :type user_id: unicode
        """
        self.__user_id = user_id

    def get_trigger_name(self):
        """
        トリガーIDを取得
        :return: トリガーID
        :rtype: unicode
        """
        return self.__trigger_name

    def set_trigger_name(self, trigger_name):
        """
        トリガーIDを設定
        :param trigger_name: トリガーID
        :type trigger_name: unicode
        """
        self.__trigger_name = trigger_name

    def get_trigger_at(self):
        """
        トリガーを引いた時間(エポック秒)を取得
        :return: トリガーを引いた時間(エポック秒)
        :rtype: int
        """
        return self.__trigger_at

    def set_trigger_at(self, trigger_at):
        """
        トリガーを引いた時間(エポック秒)を設定
        :param trigger_at: トリガーを引いた時間(エポック秒)
        :type trigger_at: int
        """
        self.__trigger_at = trigger_at

    def to_dict(self):
        return {
            "userId": self.__user_id,
            "triggerName": self.__trigger_name,
            "triggerAt": self.__trigger_at,
        }
