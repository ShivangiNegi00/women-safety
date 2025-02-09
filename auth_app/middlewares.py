from django.shortcuts import redirect #type:ignore

#********Authenticated ***********
def auth(view_function):
    def wrapeed_view(request, *args, **kwargs):
        if request.user.is_authenticated == False:
            return redirect('home') # login -> home
        return view_function(request, *args, **kwargs)
    return wrapeed_view
#********Guest***********
def guest(view_function):
    def wrapeed_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return view_function(request, *args, **kwargs)
    return wrapeed_view