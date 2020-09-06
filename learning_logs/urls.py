from django.urls import path

from . import views # this means import views from the same dirc as this file

app_name = 'learning_logs'
urlpatterns = [
	# Home page
	path('', views.index, name='index'),
	# Path for showing the topics
	path('topics/', views.topics, name='topics'),
	# Detail page for a single topic
	path('topics/<int:topic_id>/', views.topic, name='topic'),
	# Page for adding new topic
	path('new_topic/', views.new_topic, name='new_topic'),
	# Page for adding new entry
	path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
	# Page for editing an entry
	path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry')
]