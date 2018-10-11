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


class PullTriggerRequest(Gs2BasicRequest):

    class Constant(Gs2Schedule):
        FUNCTION = "PullTrigger"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(PullTriggerRequest, self).__init__(params)
        if params is None:
            self.__schedule_name = None
        else:
            self.set_schedule_name(params['scheduleName'] if 'scheduleName' in params.keys() else None)
        if params is None:
            self.__user_id = None
        else:
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
        if params is None:
            self.__trigger_name = None
        else:
            self.set_trigger_name(params['triggerName'] if 'triggerName' in params.keys() else None)
        if params is None:
            self.__action = None
        else:
            self.set_action(params['action'] if 'action' in params.keys() else None)
        if params is None:
            self.__ttl = None
        else:
            self.set_ttl(params['ttl'] if 'ttl' in params.keys() else None)

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
        if schedule_name is not None and not (isinstance(schedule_name, str) or isinstance(schedule_name, unicode)):
            raise TypeError(type(schedule_name))
        self.__schedule_name = schedule_name

    def with_schedule_name(self, schedule_name):
        """
        スケジュールの名前を指定します。を設定
        :param schedule_name: スケジュールの名前を指定します。
        :type schedule_name: unicode
        :return: this
        :rtype: PullTriggerRequest
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
        if user_id is not None and not (isinstance(user_id, str) or isinstance(user_id, unicode)):
            raise TypeError(type(user_id))
        self.__user_id = user_id

    def with_user_id(self, user_id):
        """
        ユーザIDを指定します。を設定
        :param user_id: ユーザIDを指定します。
        :type user_id: unicode
        :return: this
        :rtype: PullTriggerRequest
        """
        self.set_user_id(user_id)
        return self

    def get_trigger_name(self):
        """
        トリガーの名前を指定します。を取得
        :return: トリガーの名前を指定します。
        :rtype: unicode
        """
        return self.__trigger_name

    def set_trigger_name(self, trigger_name):
        """
        トリガーの名前を指定します。を設定
        :param trigger_name: トリガーの名前を指定します。
        :type trigger_name: unicode
        """
        if trigger_name is not None and not (isinstance(trigger_name, str) or isinstance(trigger_name, unicode)):
            raise TypeError(type(trigger_name))
        self.__trigger_name = trigger_name

    def with_trigger_name(self, trigger_name):
        """
        トリガーの名前を指定します。を設定
        :param trigger_name: トリガーの名前を指定します。
        :type trigger_name: unicode
        :return: this
        :rtype: PullTriggerRequest
        """
        self.set_trigger_name(trigger_name)
        return self

    def get_action(self):
        """
        既にトリガーが引かれていた時の振る舞いを取得
        :return: 既にトリガーが引かれていた時の振る舞い
        :rtype: unicode
        """
        return self.__action

    def set_action(self, action):
        """
        既にトリガーが引かれていた時の振る舞いを設定
        :param action: 既にトリガーが引かれていた時の振る舞い
        :type action: unicode
        """
        if action is not None and not (isinstance(action, str) or isinstance(action, unicode)):
            raise TypeError(type(action))
        self.__action = action

    def with_action(self, action):
        """
        既にトリガーが引かれていた時の振る舞いを設定
        :param action: 既にトリガーが引かれていた時の振る舞い
        :type action: unicode
        :return: this
        :rtype: PullTriggerRequest
        """
        self.set_action(action)
        return self

    def get_ttl(self):
        """
        action に if_expired_pull_again を指定したときに使用するトリガーの有効期間(分)を取得
        :return: action に if_expired_pull_again を指定したときに使用するトリガーの有効期間(分)
        :rtype: int
        """
        return self.__ttl

    def set_ttl(self, ttl):
        """
        action に if_expired_pull_again を指定したときに使用するトリガーの有効期間(分)を設定
        :param ttl: action に if_expired_pull_again を指定したときに使用するトリガーの有効期間(分)
        :type ttl: int
        """
        if ttl is not None and not isinstance(ttl, int):
            raise TypeError(type(ttl))
        self.__ttl = ttl

    def with_ttl(self, ttl):
        """
        action に if_expired_pull_again を指定したときに使用するトリガーの有効期間(分)を設定
        :param ttl: action に if_expired_pull_again を指定したときに使用するトリガーの有効期間(分)
        :type ttl: int
        :return: this
        :rtype: PullTriggerRequest
        """
        self.set_ttl(ttl)
        return self
