
#<--- My Portfolio Website - Imported Packages List ----
from django.contrib import admin
from django.urls import path,include
#</--- My Portfolio Website - Imported Packages List ----



#Admin Site Header Name
admin.site.site_header = "My Portfolio Admin"
#Admin site Title
admin.site.site_title = "My Portfolio Admin Portal"
#Admin site Index title
admin.site.index_title = "Welcome to My Portfolio Portal"





#---My Portfolio Website Admin and Data Management URL List ---
urlpatterns = [
    #Url for Admin Site
    path('admin/', admin.site.urls),

    #Url for my_portfolio_website_app configuration
    path('', include('my_portfolio_website_app.urls')),
]

#/---My Portfolio Website Admin and Data Management URL List ---
