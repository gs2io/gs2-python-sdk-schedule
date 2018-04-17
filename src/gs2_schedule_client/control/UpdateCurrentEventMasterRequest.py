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


class UpdateCurrentEventMasterRequest(Gs2BasicRequest):

    class Constant(Gs2Schedule):
        FUNCTION = "UpdateCurrentEventMaster"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(UpdateCurrentEventMasterRequest, self).__init__(params)
        if params is None:
            self.__schedule_name = None
        else:
            self.set_schedule_name(params['scheduleName'] if 'scheduleName' in params.keys() else None)
        if params is None:
            self.__settings = None
        else:
            self.set_settings(params['settings'] if 'settings' in params.keys() else None)

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
        if schedule_name and not (isinstance(schedule_name, str) or isinstance(schedule_name, unicode)):
            raise TypeError(type(schedule_name))
        self.__schedule_name = schedule_name

    def with_schedule_name(self, schedule_name):
        """
        スケジュールの名前を指定します。を設定
        :param schedule_name: スケジュールの名前を指定します。
        :type schedule_name: unicode
        :return: this
        :rtype: UpdateCurrentEventMasterRequest
        """
        self.set_schedule_name(schedule_name)
        return self

    def get_settings(self):
        """
        イベントマスターデータを取得
        :return: イベントマスターデータ
        :rtype: unicode
        """
        return self.__settings

    def set_settings(self, settings):
        """
        イベントマスターデータを設定
        :param settings: イベントマスターデータ
        :type settings: unicode
        """
        if settings and not (isinstance(settings, str) or isinstance(settings, unicode)):
            raise TypeError(type(settings))
        self.__settings = settings

    def with_settings(self, settings):
        """
        イベントマスターデータを設定
        :param settings: イベントマスターデータ
        :type settings: unicode
        :return: this
        :rtype: UpdateCurrentEventMasterRequest
        """
        self.set_settings(settings)
        return self
