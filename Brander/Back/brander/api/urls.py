from django.urls import path
from .views import UserList, UserDetail, TextAnalysisList, TextAnalysisDetail, \
    UserTextAnalysisList, TextAnalysisUserList
from .views import ObtainTokenPairView, generate_design

urlpatterns = [
    path('users/', UserList.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('text-analyses/', TextAnalysisList.as_view(), name='text_analysis_list'),
    path('text-analyses/<int:pk>/', TextAnalysisDetail.as_view(), name='text_analysis_detail'),
    path('users/<int:user_id>/text-analyses/', UserTextAnalysisList.as_view(), name='user_text_analysis_list'),
    path('text-analyses/<int:text_analysis_id>/user/', TextAnalysisUserList.as_view(), name='text_analysis_user'),
    path('api/token/', ObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('generate_design/', generate_design, name='generate_design'),

]
