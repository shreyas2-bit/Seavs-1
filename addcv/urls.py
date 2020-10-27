from django.urls import path
from . import views


urlpatterns = [
     path('personal/', views.personal,name='personal'), #personal form
     path('updatepersonal/<int:person_id>', views.updatepersonal,name='updatepersonal'),
     path('deletepersonal/<int:person_id>', views.deletepersonal,name='deletepersonal'),
     path('education/<int:person_id>', views.educational,name='ed'),   #education form
     path('experiences/<int:person_id>', views.experiences, name='ex'),  #job form
     path('skill/<int:person_id>', views.skill_person,name='skill'),
     path('project/<int:person_id>', views.project, name='project'),  #project form
     path('upproject/<int:person_id>/<int:pro_id>', views.upproject, name='updateprojects'),
     path('updateeducation/<int:person_id>/<int:edu_id>', views.updateeducation, name='updateeducation'),
     path('deleteeducation/<int:person_id>/<int:edu_id>', views.deleteeducation, name='deleteeducation'),
     path('updateexperience/<int:person_id>/<int:exp_id>', views.updateexperience, name='updateexperience'),
     path('deleteexperience/<int:person_id>/<int:exp_id>', views.deleteexperience, name='deleteexperience'),
     path('',views.createcv, name='create-cv-page'),    #createcv page
     path('persondash/<int:person_id>', views.personaldash, name='persondash'),
     path('showcv/<int:person_id>', views.showcv, name='showcv'),
     path('mycv/<int:person_id>/<int:my_id>', views.mycv, name='mycv'),
     path('userdash/', views.dashboard,name='dashboard'),
   #   path('madecv/',views.cv,name='cv'),                #cv2
    #  path('export-pdf', views.export_pdf, name='export-pdf'),
 ]
