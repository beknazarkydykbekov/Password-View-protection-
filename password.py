# view.py
class AccreditationView(View):
    def get(self, request, *args, **kwargs):
        form = PasswordForm(request.POST or None)
        files = File.objects.all()
        context = {
            'form': form,
            'files': files
        }
        return render(request, 'pricing.html', context)

    def post(self, request, *args, **kwargs):
        form = PasswordForm(request.POST or None)
        if form.is_valid():
            password_check = form.save(commit=False)
            password_check.password = form.cleaned_data['password']
            if password_check.password == ACCREDITATION_PASSWORD:
                return render(request, 'accreditation_check.html')
        context = {
            'form': form,
        }
        return render(request, 'pricing.html', context)
        
        
        
        
# forms.py
class PasswordForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].label = 'Пароль'

    def check_password(self):
        password = self.cleaned_data['password']
        if password != ACCREDITATION_PASSWORD:
            raise forms.ValidationError(
                'Неправильный пароль! Попробуйте еще.'
            )
        return password

    class Meta:
        model = User
        fields = (
            'password',
        )








# template
<section class="schedule_page text_page section">
		<div class="container"><h1 class="section_title">Защищено: Аккредитация</h1>
			<div class="text">
				<form role="form" action="{% url 'accreditation' %}" method="POST">
					{% csrf_token %}
				<p>Это содержимое защищено паролем. Для его просмотра введите, пожалуйста, пароль:</p>
				<p>Пароль: <input type="password" id="password" name="password"/></p>
					<input type="submit" value="Войти" /></p>
				</form>
			</div>
		</div>
	</section>





