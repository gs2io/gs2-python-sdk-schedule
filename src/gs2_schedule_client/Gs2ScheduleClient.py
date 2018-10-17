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

from gs2_core_client.Gs2Constant import Gs2Constant
from gs2_core_client.AbstractGs2Client import AbstractGs2Client
from aws_sdk_for_serverless.common import url_encoder


class Gs2ScheduleClient(AbstractGs2Client):

    ENDPOINT = "schedule"

    def __init__(self, credential, region):
        """
        コンストラクタ
        :param credential: 認証情報
        :type credential: IGs2Credential
        :param region: GS2リージョン
        :type region: str
        """
        super(Gs2ScheduleClient, self).__init__(credential, region)

    def get_current_event_master(self, request):
        """
        現在適用されているイベントマスターを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_schedule_client.control.GetCurrentEventMasterRequest.GetCurrentEventMasterRequest
        :return: 結果
        :rtype: gs2_schedule_client.control.GetCurrentEventMasterResult.GetCurrentEventMasterResult
        """
        query_strings = {}
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_schedule_client.control.GetCurrentEventMasterRequest import GetCurrentEventMasterRequest

        from gs2_schedule_client.control.GetCurrentEventMasterResult import GetCurrentEventMasterResult
        return GetCurrentEventMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/schedule/" + str(("null" if request.get_schedule_name() is None or request.get_schedule_name() == "" else request.get_schedule_name())) + "/event/master",
            service=self.ENDPOINT,
            component=GetCurrentEventMasterRequest.Constant.MODULE,
            target_function=GetCurrentEventMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def update_current_event_master(self, request):
        """
        イベントマスターを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_schedule_client.control.UpdateCurrentEventMasterRequest.UpdateCurrentEventMasterRequest
        :return: 結果
        :rtype: gs2_schedule_client.control.UpdateCurrentEventMasterResult.UpdateCurrentEventMasterResult
        """
        body = { 
            "settings": request.get_settings(),
        }

        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_schedule_client.control.UpdateCurrentEventMasterRequest import UpdateCurrentEventMasterRequest
        from gs2_schedule_client.control.UpdateCurrentEventMasterResult import UpdateCurrentEventMasterResult
        return UpdateCurrentEventMasterResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/schedule/" + str(("null" if request.get_schedule_name() is None or request.get_schedule_name() == "" else request.get_schedule_name())) + "/event/master",
            service=self.ENDPOINT,
            component=UpdateCurrentEventMasterRequest.Constant.MODULE,
            target_function=UpdateCurrentEventMasterRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def create_event_master(self, request):
        """
        イベントマスターを新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_schedule_client.control.CreateEventMasterRequest.CreateEventMasterRequest
        :return: 結果
        :rtype: gs2_schedule_client.control.CreateEventMasterResult.CreateEventMasterResult
        """
        body = { 
            "name": request.get_name(),
            "type": request.get_type(),
        }

        if request.get_meta() is not None:
            body["meta"] = request.get_meta()
        if request.get_absolute_begin() is not None:
            body["absoluteBegin"] = request.get_absolute_begin()
        if request.get_absolute_end() is not None:
            body["absoluteEnd"] = request.get_absolute_end()
        if request.get_relative_trigger_name() is not None:
            body["relativeTriggerName"] = request.get_relative_trigger_name()
        if request.get_relative_span() is not None:
            body["relativeSpan"] = request.get_relative_span()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_schedule_client.control.CreateEventMasterRequest import CreateEventMasterRequest
        from gs2_schedule_client.control.CreateEventMasterResult import CreateEventMasterResult
        return CreateEventMasterResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/schedule/" + str(("null" if request.get_schedule_name() is None or request.get_schedule_name() == "" else request.get_schedule_name())) + "/master/event",
            service=self.ENDPOINT,
            component=CreateEventMasterRequest.Constant.MODULE,
            target_function=CreateEventMasterRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_event_master(self, request):
        """
        イベントマスターを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_schedule_client.control.DeleteEventMasterRequest.DeleteEventMasterRequest
        """
        query_strings = {}
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_schedule_client.control.DeleteEventMasterRequest import DeleteEventMasterRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/schedule/" + str(("null" if request.get_schedule_name() is None or request.get_schedule_name() == "" else request.get_schedule_name())) + "/master/event/" + str(("null" if request.get_event_name() is None or request.get_event_name() == "" else request.get_event_name())) + "",
            service=self.ENDPOINT,
            component=DeleteEventMasterRequest.Constant.MODULE,
            target_function=DeleteEventMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_event_master(self, request):
        """
        イベントマスターの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_schedule_client.control.DescribeEventMasterRequest.DescribeEventMasterRequest
        :return: 結果
        :rtype: gs2_schedule_client.control.DescribeEventMasterResult.DescribeEventMasterResult
        """
        query_strings = {}
        if request.get_page_token() is not None:
            query_strings['pageToken'] = request.get_page_token()
        if request.get_limit() is not None:
            query_strings['limit'] = request.get_limit()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_schedule_client.control.DescribeEventMasterRequest import DescribeEventMasterRequest

        from gs2_schedule_client.control.DescribeEventMasterResult import DescribeEventMasterResult
        return DescribeEventMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/schedule/" + str(("null" if request.get_schedule_name() is None or request.get_schedule_name() == "" else request.get_schedule_name())) + "/master/event",
            service=self.ENDPOINT,
            component=DescribeEventMasterRequest.Constant.MODULE,
            target_function=DescribeEventMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_event_master(self, request):
        """
        イベントマスターを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_schedule_client.control.GetEventMasterRequest.GetEventMasterRequest
        :return: 結果
        :rtype: gs2_schedule_client.control.GetEventMasterResult.GetEventMasterResult
        """
        query_strings = {}
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_schedule_client.control.GetEventMasterRequest import GetEventMasterRequest

        from gs2_schedule_client.control.GetEventMasterResult import GetEventMasterResult
        return GetEventMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/schedule/" + str(("null" if request.get_schedule_name() is None or request.get_schedule_name() == "" else request.get_schedule_name())) + "/master/event/" + str(("null" if request.get_event_name() is None or request.get_event_name() == "" else request.get_event_name())) + "",
            service=self.ENDPOINT,
            component=GetEventMasterRequest.Constant.MODULE,
            target_function=GetEventMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def update_event_master(self, request):
        """
        イベントマスターを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_schedule_client.control.UpdateEventMasterRequest.UpdateEventMasterRequest
        :return: 結果
        :rtype: gs2_schedule_client.control.UpdateEventMasterResult.UpdateEventMasterResult
        """
        body = { 
            "type": request.get_type(),
        }
        if request.get_meta() is not None:
            body["meta"] = request.get_meta()
        if request.get_absolute_begin() is not None:
            body["absoluteBegin"] = request.get_absolute_begin()
        if request.get_absolute_end() is not None:
            body["absoluteEnd"] = request.get_absolute_end()
        if request.get_relative_trigger_name() is not None:
            body["relativeTriggerName"] = request.get_relative_trigger_name()
        if request.get_relative_span() is not None:
            body["relativeSpan"] = request.get_relative_span()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_schedule_client.control.UpdateEventMasterRequest import UpdateEventMasterRequest
        from gs2_schedule_client.control.UpdateEventMasterResult import UpdateEventMasterResult
        return UpdateEventMasterResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/schedule/" + str(("null" if request.get_schedule_name() is None or request.get_schedule_name() == "" else request.get_schedule_name())) + "/master/event/" + str(("null" if request.get_event_name() is None or request.get_event_name() == "" else request.get_event_name())) + "",
            service=self.ENDPOINT,
            component=UpdateEventMasterRequest.Constant.MODULE,
            target_function=UpdateEventMasterRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def describe_event(self, request):
        """
        開催中のイベントの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_schedule_client.control.DescribeEventRequest.DescribeEventRequest
        :return: 結果
        :rtype: gs2_schedule_client.control.DescribeEventResult.DescribeEventResult
        """
        query_strings = {}
        if request.get_event_names() is not None:
            query_strings['eventNames'] = u','.join(request.get_event_names())
        headers = {}
        if request.get_access_token() is not None:
            headers["X-GS2-ACCESS-TOKEN"] = request.get_access_token()
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_schedule_client.control.DescribeEventRequest import DescribeEventRequest

        from gs2_schedule_client.control.DescribeEventResult import DescribeEventResult
        return DescribeEventResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/schedule/" + str(("null" if request.get_schedule_name() is None or request.get_schedule_name() == "" else request.get_schedule_name())) + "/event",
            service=self.ENDPOINT,
            component=DescribeEventRequest.Constant.MODULE,
            target_function=DescribeEventRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def describe_event_by_user_id(self, request):
        """
        開催中のイベントの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_schedule_client.control.DescribeEventByUserIdRequest.DescribeEventByUserIdRequest
        :return: 結果
        :rtype: gs2_schedule_client.control.DescribeEventByUserIdResult.DescribeEventByUserIdResult
        """
        query_strings = {}
        if request.get_event_names() is not None:
            query_strings['eventNames'] = u','.join(request.get_event_names())
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_schedule_client.control.DescribeEventByUserIdRequest import DescribeEventByUserIdRequest

        from gs2_schedule_client.control.DescribeEventByUserIdResult import DescribeEventByUserIdResult
        return DescribeEventByUserIdResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/schedule/" + str(("null" if request.get_schedule_name() is None or request.get_schedule_name() == "" else request.get_schedule_name())) + "/event/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else request.get_user_id())) + "",
            service=self.ENDPOINT,
            component=DescribeEventByUserIdRequest.Constant.MODULE,
            target_function=DescribeEventByUserIdRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_event(self, request):
        """
        開催中のイベントを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_schedule_client.control.GetEventRequest.GetEventRequest
        :return: 結果
        :rtype: gs2_schedule_client.control.GetEventResult.GetEventResult
        """
        query_strings = {}
        headers = {}
        if request.get_access_token() is not None:
            headers["X-GS2-ACCESS-TOKEN"] = request.get_access_token()
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_schedule_client.control.GetEventRequest import GetEventRequest

        from gs2_schedule_client.control.GetEventResult import GetEventResult
        return GetEventResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/schedule/" + str(("null" if request.get_schedule_name() is None or request.get_schedule_name() == "" else request.get_schedule_name())) + "/event/" + str(("null" if request.get_event_name() is None or request.get_event_name() == "" else request.get_event_name())) + "",
            service=self.ENDPOINT,
            component=GetEventRequest.Constant.MODULE,
            target_function=GetEventRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_event_by_user_id(self, request):
        """
        開催中のイベントを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_schedule_client.control.GetEventByUserIdRequest.GetEventByUserIdRequest
        :return: 結果
        :rtype: gs2_schedule_client.control.GetEventByUserIdResult.GetEventByUserIdResult
        """
        query_strings = {}
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_schedule_client.control.GetEventByUserIdRequest import GetEventByUserIdRequest

        from gs2_schedule_client.control.GetEventByUserIdResult import GetEventByUserIdResult
        return GetEventByUserIdResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/schedule/" + str(("null" if request.get_schedule_name() is None or request.get_schedule_name() == "" else request.get_schedule_name())) + "/event/" + str(("null" if request.get_event_name() is None or request.get_event_name() == "" else request.get_event_name())) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else request.get_user_id())) + "",
            service=self.ENDPOINT,
            component=GetEventByUserIdRequest.Constant.MODULE,
            target_function=GetEventByUserIdRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def export_master(self, request):
        """
        イベントマスターをエクスポートします<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_schedule_client.control.ExportMasterRequest.ExportMasterRequest
        :return: 結果
        :rtype: gs2_schedule_client.control.ExportMasterResult.ExportMasterResult
        """
        query_strings = {}
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_schedule_client.control.ExportMasterRequest import ExportMasterRequest

        from gs2_schedule_client.control.ExportMasterResult import ExportMasterResult
        return ExportMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/schedule/" + str(("null" if request.get_schedule_name() is None or request.get_schedule_name() == "" else request.get_schedule_name())) + "/master",
            service=self.ENDPOINT,
            component=ExportMasterRequest.Constant.MODULE,
            target_function=ExportMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def create_schedule(self, request):
        """
        スケジュールを新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_schedule_client.control.CreateScheduleRequest.CreateScheduleRequest
        :return: 結果
        :rtype: gs2_schedule_client.control.CreateScheduleResult.CreateScheduleResult
        """
        body = { 
            "name": request.get_name(),
        }

        if request.get_description() is not None:
            body["description"] = request.get_description()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_schedule_client.control.CreateScheduleRequest import CreateScheduleRequest
        from gs2_schedule_client.control.CreateScheduleResult import CreateScheduleResult
        return CreateScheduleResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/schedule",
            service=self.ENDPOINT,
            component=CreateScheduleRequest.Constant.MODULE,
            target_function=CreateScheduleRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_schedule(self, request):
        """
        スケジュールを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_schedule_client.control.DeleteScheduleRequest.DeleteScheduleRequest
        """
        query_strings = {}
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_schedule_client.control.DeleteScheduleRequest import DeleteScheduleRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/schedule/" + str(("null" if request.get_schedule_name() is None or request.get_schedule_name() == "" else request.get_schedule_name())) + "",
            service=self.ENDPOINT,
            component=DeleteScheduleRequest.Constant.MODULE,
            target_function=DeleteScheduleRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_schedule(self, request):
        """
        スケジュールの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_schedule_client.control.DescribeScheduleRequest.DescribeScheduleRequest
        :return: 結果
        :rtype: gs2_schedule_client.control.DescribeScheduleResult.DescribeScheduleResult
        """
        query_strings = {}
        if request.get_page_token() is not None:
            query_strings['pageToken'] = request.get_page_token()
        if request.get_limit() is not None:
            query_strings['limit'] = request.get_limit()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_schedule_client.control.DescribeScheduleRequest import DescribeScheduleRequest

        from gs2_schedule_client.control.DescribeScheduleResult import DescribeScheduleResult
        return DescribeScheduleResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/schedule",
            service=self.ENDPOINT,
            component=DescribeScheduleRequest.Constant.MODULE,
            target_function=DescribeScheduleRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_schedule(self, request):
        """
        スケジュールを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_schedule_client.control.GetScheduleRequest.GetScheduleRequest
        :return: 結果
        :rtype: gs2_schedule_client.control.GetScheduleResult.GetScheduleResult
        """
        query_strings = {}
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_schedule_client.control.GetScheduleRequest import GetScheduleRequest

        from gs2_schedule_client.control.GetScheduleResult import GetScheduleResult
        return GetScheduleResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/schedule/" + str(("null" if request.get_schedule_name() is None or request.get_schedule_name() == "" else request.get_schedule_name())) + "",
            service=self.ENDPOINT,
            component=GetScheduleRequest.Constant.MODULE,
            target_function=GetScheduleRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_schedule_status(self, request):
        """
        スケジュールの状態を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_schedule_client.control.GetScheduleStatusRequest.GetScheduleStatusRequest
        :return: 結果
        :rtype: gs2_schedule_client.control.GetScheduleStatusResult.GetScheduleStatusResult
        """
        query_strings = {}
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_schedule_client.control.GetScheduleStatusRequest import GetScheduleStatusRequest

        from gs2_schedule_client.control.GetScheduleStatusResult import GetScheduleStatusResult
        return GetScheduleStatusResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/schedule/" + str(("null" if request.get_schedule_name() is None or request.get_schedule_name() == "" else request.get_schedule_name())) + "/status",
            service=self.ENDPOINT,
            component=GetScheduleStatusRequest.Constant.MODULE,
            target_function=GetScheduleStatusRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def update_schedule(self, request):
        """
        スケジュールを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_schedule_client.control.UpdateScheduleRequest.UpdateScheduleRequest
        :return: 結果
        :rtype: gs2_schedule_client.control.UpdateScheduleResult.UpdateScheduleResult
        """
        body = { 
        }
        if request.get_description() is not None:
            body["description"] = request.get_description()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_schedule_client.control.UpdateScheduleRequest import UpdateScheduleRequest
        from gs2_schedule_client.control.UpdateScheduleResult import UpdateScheduleResult
        return UpdateScheduleResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/schedule/" + str(("null" if request.get_schedule_name() is None or request.get_schedule_name() == "" else request.get_schedule_name())) + "",
            service=self.ENDPOINT,
            component=UpdateScheduleRequest.Constant.MODULE,
            target_function=UpdateScheduleRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_trigger(self, request):
        """
        トリガーを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_schedule_client.control.DeleteTriggerRequest.DeleteTriggerRequest
        """
        query_strings = {}
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_schedule_client.control.DeleteTriggerRequest import DeleteTriggerRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/schedule/" + str(("null" if request.get_schedule_name() is None or request.get_schedule_name() == "" else request.get_schedule_name())) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else request.get_user_id())) + "/trigger/" + str(("null" if request.get_trigger_name() is None or request.get_trigger_name() == "" else request.get_trigger_name())) + "",
            service=self.ENDPOINT,
            component=DeleteTriggerRequest.Constant.MODULE,
            target_function=DeleteTriggerRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_trigger(self, request):
        """
        トリガーの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_schedule_client.control.DescribeTriggerRequest.DescribeTriggerRequest
        :return: 結果
        :rtype: gs2_schedule_client.control.DescribeTriggerResult.DescribeTriggerResult
        """
        query_strings = {}
        if request.get_page_token() is not None:
            query_strings['pageToken'] = request.get_page_token()
        if request.get_limit() is not None:
            query_strings['limit'] = request.get_limit()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_schedule_client.control.DescribeTriggerRequest import DescribeTriggerRequest

        from gs2_schedule_client.control.DescribeTriggerResult import DescribeTriggerResult
        return DescribeTriggerResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/schedule/" + str(("null" if request.get_schedule_name() is None or request.get_schedule_name() == "" else request.get_schedule_name())) + "/trigger",
            service=self.ENDPOINT,
            component=DescribeTriggerRequest.Constant.MODULE,
            target_function=DescribeTriggerRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def describe_trigger_by_user_id(self, request):
        """
        ユーザのトリガーの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_schedule_client.control.DescribeTriggerByUserIdRequest.DescribeTriggerByUserIdRequest
        :return: 結果
        :rtype: gs2_schedule_client.control.DescribeTriggerByUserIdResult.DescribeTriggerByUserIdResult
        """
        query_strings = {}
        if request.get_page_token() is not None:
            query_strings['pageToken'] = request.get_page_token()
        if request.get_limit() is not None:
            query_strings['limit'] = request.get_limit()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_schedule_client.control.DescribeTriggerByUserIdRequest import DescribeTriggerByUserIdRequest

        from gs2_schedule_client.control.DescribeTriggerByUserIdResult import DescribeTriggerByUserIdResult
        return DescribeTriggerByUserIdResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/schedule/" + str(("null" if request.get_schedule_name() is None or request.get_schedule_name() == "" else request.get_schedule_name())) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else request.get_user_id())) + "/trigger",
            service=self.ENDPOINT,
            component=DescribeTriggerByUserIdRequest.Constant.MODULE,
            target_function=DescribeTriggerByUserIdRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_trigger(self, request):
        """
        トリガーを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_schedule_client.control.GetTriggerRequest.GetTriggerRequest
        :return: 結果
        :rtype: gs2_schedule_client.control.GetTriggerResult.GetTriggerResult
        """
        query_strings = {}
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_schedule_client.control.GetTriggerRequest import GetTriggerRequest

        from gs2_schedule_client.control.GetTriggerResult import GetTriggerResult
        return GetTriggerResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/schedule/" + str(("null" if request.get_schedule_name() is None or request.get_schedule_name() == "" else request.get_schedule_name())) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else request.get_user_id())) + "/trigger/" + str(("null" if request.get_trigger_name() is None or request.get_trigger_name() == "" else request.get_trigger_name())) + "",
            service=self.ENDPOINT,
            component=GetTriggerRequest.Constant.MODULE,
            target_function=GetTriggerRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def pull_trigger(self, request):
        """
        トリガーを引きます<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_schedule_client.control.PullTriggerRequest.PullTriggerRequest
        :return: 結果
        :rtype: gs2_schedule_client.control.PullTriggerResult.PullTriggerResult
        """
        body = { 
            "action": request.get_action(),
        }
        if request.get_ttl() is not None:
            body["ttl"] = request.get_ttl()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_schedule_client.control.PullTriggerRequest import PullTriggerRequest
        from gs2_schedule_client.control.PullTriggerResult import PullTriggerResult
        return PullTriggerResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/schedule/" + str(("null" if request.get_schedule_name() is None or request.get_schedule_name() == "" else request.get_schedule_name())) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else request.get_user_id())) + "/trigger/" + str(("null" if request.get_trigger_name() is None or request.get_trigger_name() == "" else request.get_trigger_name())) + "",
            service=self.ENDPOINT,
            component=PullTriggerRequest.Constant.MODULE,
            target_function=PullTriggerRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))
