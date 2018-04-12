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


class UpdateEventMasterRequest(Gs2BasicRequest):

    class Constant(Gs2Schedule):
        FUNCTION = "UpdateEventMaster"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(UpdateEventMasterRequest, self).__init__(params)
        if params is None:
            self.__schedule_name = None
        else:
            self.set_schedule_name(params['scheduleName'] if 'scheduleName' in params.keys() else None)
        if params is None:
            self.__event_name = None
        else:
            self.set_event_name(params['eventName'] if 'eventName' in params.keys() else None)
        if params is None:
            self.__meta = None
        else:
            self.set_meta(params['meta'] if 'meta' in params.keys() else None)
        if params is None:
            self.__type = None
        else:
            self.set_type(params['type'] if 'type' in params.keys() else None)
        if params is None:
            self.__absolute_begin = None
        else:
            self.set_absolute_begin(params['absoluteBegin'] if 'absoluteBegin' in params.keys() else None)
        if params is None:
            self.__absolute_end = None
        else:
            self.set_absolute_end(params['absoluteEnd'] if 'absoluteEnd' in params.keys() else None)
        if params is None:
            self.__relative_trigger_name = None
        else:
            self.set_relative_trigger_name(params['relativeTriggerName'] if 'relativeTriggerName' in params.keys() else None)
        if params is None:
            self.__relative_span = None
        else:
            self.set_relative_span(params['relativeSpan'] if 'relativeSpan' in params.keys() else None)

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
        if not isinstance(schedule_name, unicode):
            raise TypeError(type(schedule_name))
        self.__schedule_name = schedule_name

    def with_schedule_name(self, schedule_name):
        """
        スケジュールの名前を指定します。を設定
        :param schedule_name: スケジュールの名前を指定します。
        :type schedule_name: unicode
        :return: this
        :rtype: UpdateEventMasterRequest
        """
        self.set_schedule_name(schedule_name)
        return self

    def get_event_name(self):
        """
        イベント名を指定します。を取得
        :return: イベント名を指定します。
        :rtype: unicode
        """
        return self.__event_name

    def set_event_name(self, event_name):
        """
        イベント名を指定します。を設定
        :param event_name: イベント名を指定します。
        :type event_name: unicode
        """
        if not isinstance(event_name, unicode):
            raise TypeError(type(event_name))
        self.__event_name = event_name

    def with_event_name(self, event_name):
        """
        イベント名を指定します。を設定
        :param event_name: イベント名を指定します。
        :type event_name: unicode
        :return: this
        :rtype: UpdateEventMasterRequest
        """
        self.set_event_name(event_name)
        return self

    def get_meta(self):
        """
        メタデータを取得
        :return: メタデータ
        :rtype: unicode
        """
        return self.__meta

    def set_meta(self, meta):
        """
        メタデータを設定
        :param meta: メタデータ
        :type meta: unicode
        """
        if not isinstance(meta, unicode):
            raise TypeError(type(meta))
        self.__meta = meta

    def with_meta(self, meta):
        """
        メタデータを設定
        :param meta: メタデータ
        :type meta: unicode
        :return: this
        :rtype: UpdateEventMasterRequest
        """
        self.set_meta(meta)
        return self

    def get_absolute_begin(self):
        """
        絶対時間を選択した場合の開始日時を取得
        :return: 絶対時間を選択した場合の開始日時
        :rtype: int
        """
        return self.__absolute_begin

    def set_absolute_begin(self, absolute_begin):
        """
        絶対時間を選択した場合の開始日時を設定
        :param absolute_begin: 絶対時間を選択した場合の開始日時
        :type absolute_begin: int
        """
        if not isinstance(absolute_begin, int):
            raise TypeError(type(absolute_begin))
        self.__absolute_begin = absolute_begin

    def with_absolute_begin(self, absolute_begin):
        """
        絶対時間を選択した場合の開始日時を設定
        :param absolute_begin: 絶対時間を選択した場合の開始日時
        :type absolute_begin: int
        :return: this
        :rtype: UpdateEventMasterRequest
        """
        self.set_absolute_begin(absolute_begin)
        return self

    def get_absolute_end(self):
        """
        絶対時間を選択した場合の終了日時を取得
        :return: 絶対時間を選択した場合の終了日時
        :rtype: int
        """
        return self.__absolute_end

    def set_absolute_end(self, absolute_end):
        """
        絶対時間を選択した場合の終了日時を設定
        :param absolute_end: 絶対時間を選択した場合の終了日時
        :type absolute_end: int
        """
        if not isinstance(absolute_end, int):
            raise TypeError(type(absolute_end))
        self.__absolute_end = absolute_end

    def with_absolute_end(self, absolute_end):
        """
        絶対時間を選択した場合の終了日時を設定
        :param absolute_end: 絶対時間を選択した場合の終了日時
        :type absolute_end: int
        :return: this
        :rtype: UpdateEventMasterRequest
        """
        self.set_absolute_end(absolute_end)
        return self

    def get_relative_trigger_name(self):
        """
        相対時間を選択した場合の開始トリガー名を取得
        :return: 相対時間を選択した場合の開始トリガー名
        :rtype: unicode
        """
        return self.__relative_trigger_name

    def set_relative_trigger_name(self, relative_trigger_name):
        """
        相対時間を選択した場合の開始トリガー名を設定
        :param relative_trigger_name: 相対時間を選択した場合の開始トリガー名
        :type relative_trigger_name: unicode
        """
        if not isinstance(relative_trigger_name, unicode):
            raise TypeError(type(relative_trigger_name))
        self.__relative_trigger_name = relative_trigger_name

    def with_relative_trigger_name(self, relative_trigger_name):
        """
        相対時間を選択した場合の開始トリガー名を設定
        :param relative_trigger_name: 相対時間を選択した場合の開始トリガー名
        :type relative_trigger_name: unicode
        :return: this
        :rtype: UpdateEventMasterRequest
        """
        self.set_relative_trigger_name(relative_trigger_name)
        return self

    def get_relative_span(self):
        """
        相対時間を選択した場合のトリガーを引いてからのイベント期間(分)を取得
        :return: 相対時間を選択した場合のトリガーを引いてからのイベント期間(分)
        :rtype: int
        """
        return self.__relative_span

    def set_relative_span(self, relative_span):
        """
        相対時間を選択した場合のトリガーを引いてからのイベント期間(分)を設定
        :param relative_span: 相対時間を選択した場合のトリガーを引いてからのイベント期間(分)
        :type relative_span: int
        """
        if not isinstance(relative_span, int):
            raise TypeError(type(relative_span))
        self.__relative_span = relative_span

    def with_relative_span(self, relative_span):
        """
        相対時間を選択した場合のトリガーを引いてからのイベント期間(分)を設定
        :param relative_span: 相対時間を選択した場合のトリガーを引いてからのイベント期間(分)
        :type relative_span: int
        :return: this
        :rtype: UpdateEventMasterRequest
        """
        self.set_relative_span(relative_span)
        return self

    def get_type(self):
        """
        期間を取得
        :return: 期間
        :rtype: unicode
        """
        return self.__type

    def set_type(self, _type):
        """
        期間を設定
        :param _type: 期間
        :type _type: unicode
        """
        if not isinstance(_type, unicode):
            raise TypeError(type(_type))
        self.__type = _type

    def with_type(self, _type):
        """
        期間を設定
        :param _type: 期間
        :type _type: unicode
        :return: this
        :rtype: UpdateEventMasterRequest
        """
        self.set_type(_type)
        return self
