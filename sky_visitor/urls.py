# Copyright 2013 Concentric Sky, Inc.
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
from django.urls import path, re_path

from sky_visitor.views import *

TOKEN_REGEX = (
    "(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})"
)

urlpatterns = [
    # re_path(r'^register/$', RegisterView.as_view(), name='register'),
    re_path(r"^login/$", LoginView.as_view(), name="login"),
    re_path(r"^logout/$", LogoutView.as_view(), name="logout"),
    re_path(
        r"^forgot_password/$", ForgotPasswordView.as_view(), name="forgot_password"
    ),
    re_path(
        r"^forgot_password/check_email/$",
        ForgotPasswordCheckEmailView.as_view(),
        name="forgot_password_check_email",
    ),
    path(
        "reset_password/<uidb36>/<token>",
        ResetPasswordView.as_view(),
        name="reset_password",
    ),
    # re_path(
    #     r"^change_password/$", ChangePasswordView.as_view(), name="change_password"
    # ),
    # re_path(r"invitation/$", InvitationStartView.as_view(), name="invitation_start"),
    # re_path(
    #     r"invitation/%s/$" % TOKEN_REGEX,
    #     InvitationCompleteView.as_view(),
    #     name="invitation_complete",
    # ),
    #     re_path(r'invitation/done/$',   InvitationDoneView.as_view(),   name='invitation_done'),
]
