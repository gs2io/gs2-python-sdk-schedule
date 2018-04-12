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

from gs2_core_client.Gs2BasicRequest import Gs2BasicRequest
from gs2_schedule_client.Gs2Schedule import Gs2Schedule


class DescribeEventByUserIdRequest(Gs2BasicRequest):

    class Constant(Gs2Schedule):
        FUNCTION = "DescribeEventByUserId"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(DescribeEventByUserIdRequest, self).__init__(params)
        if params is None:
            self.__schedule_name = None
        else:
            self.set_schedule_name(params['scheduleName'] if 'scheduleName' in params.keys() else None)
        if params is None:
            self.__user_id = None
        else:
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
        if params is None:
            self.__event_names = None
        else:
            self.set_event_names(params['eventNames'] if 'eventNames' in params.keys() else None)

    def get_schedule_name(self):
        """
        スケジュールの名前を指定します。を取得
        :return: スケジュールの名前を指定します。
        :rtype: unicode
        """
        return self.__schedule_name

    def set_schedule_name(self, schedule_name):
        """
        スケジュールの名前を指定します。を設定
        :param schedule_name: スケジュールの名前を指定します。
        :type schedule_name: unicode
        """
        if schedule_name and not isinstance(schedule_name, unicode):
            raise TypeError(type(schedule_name))
        self.__schedule_name = schedule_name

    def with_schedule_name(self, schedule_name):
        """
        スケジュールの名前を指定します。を設定
        :param schedule_name: スケジュールの名前を指定します。
        :type schedule_name: unicode
        :return: this
        :rtype: DescribeEventByUserIdRequest
        """
        self.set_schedule_name(schedule_name)
        return self

    def get_user_id(self):
        """
        ユーザIDを指定します。を取得
        :return: ユーザIDを指定します。
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        ユーザIDを指定します。を設定
        :param user_id: ユーザIDを指定します。
        :type user_id: unicode
        """
        if user_id and not isinstance(user_id, unicode):
            raise TypeError(type(user_id))
        self.__user_id = user_id

    def with_user_id(self, user_id):
        """
        ユーザIDを指定します。を設定
        :param user_id: ユーザIDを指定します。
        :type user_id: unicode
        :return: this
        :rtype: DescribeEventByUserIdRequest
        """
        self.set_user_id(user_id)
        return self

    def get_event_names(self):
        """
        取得するイベント名をカンマ区切りのリストで指定するを取得
        :return: 取得するイベント名をカンマ区切りのリストで指定する
        :rtype: unicode
        """
        return self.__event_names

    def set_event_names(self, event_names):
        """
        取得するイベント名をカンマ区切りのリストで指定するを設定
        :param event_names: 取得するイベント名をカンマ区切りのリストで指定する
        :type event_names: unicode
        """
        if event_names and not isinstance(event_names, unicode):
            raise TypeError(type(event_names))
        self.__event_names = event_names

    def with_event_names(self, event_names):
        """
        取得するイベント名をカンマ区切りのリストで指定するを設定
        :param event_names: 取得するイベント名をカンマ区切りのリストで指定する
        :type event_names: unicode
        :return: this
        :rtype: DescribeEventByUserIdRequest
        """
        self.set_event_names(event_names)
        return self
