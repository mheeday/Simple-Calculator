from django.shortcuts import render

context = {'buttons':[9,8,7,6,5,4,3,2,1], 'f_buttons': ['Delete', 'Clear'],'null_button': [0,'.'], 'action_buttons': ['/','*','-','+'], "eq_button":['='], "Input" : 'Input: '}

# Create your views here.
def home(request):
    context['Output'] = 0   
    if request.method == 'POST':
        if '=' in request.POST.keys():
            try:
                _, num_part = context['Input'].split(":")
                num_part = num_part.strip()
                solution = eval(num_part)
                context['Output'] = f"Output: {solution}"
            except:
                context['Output'] = ' ERROR! '
            finally:
                context['Input'] = 'Input: '
        elif 'Clear' in request.POST.keys():
            context['Input'] = 'Input: '
        
        elif 'Delete' in request.POST.keys():
            if context['Input'] != 'Input: ':
                context['Input'] = context['Input'][:-1]

        else:
            user_input = list(request.POST.keys())[1]
            context['Input']+= user_input
    return render(request, 'calc/home.html', context)