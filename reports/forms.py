from django import forms
from .models import Report
from datetime import date

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            'on_date',
			'daily_title',
            'daily_comment',
            'weekly_target',
            'achievement_score',
            'achievement_comment',
			'goods',
			'mores',
			'nexts'
        ]  # フォームに出したいフィールドを書く
        widgets = {
            'on_date': forms.DateInput(attrs={'type': 'date', 'class': 'input block w-full text-lg'}),
            'daily_title': forms.TextInput(attrs={'class': 'input input-ghost text-lg', 'placeholder': '今日の一言'}),
			'daily_comment': forms.Textarea(attrs={'rows': 3, 'class': 'textarea textarea_bordered h-24 w-full', 'placeholder': '今日の一言を記入'}),
            'weekly_target': forms.Textarea(attrs={'rows': 3, 'class': 'textarea textarea_bordered h-24 w-full'}),
            'achievement_score': forms.Select(choices=Report.AchievementScoreChoices, attrs={'rows': 3, 'class': 'select select-ghost'}),
            'achievement_comment': forms.Textarea(attrs={'rows': 3, 'class': 'textarea textarea_bordered h-24 w-full'}),
            'goods': forms.Textarea(attrs={'rows': 3, 'class': 'textarea textarea_bordered h-24 w-full'}),
            'mores': forms.Textarea(attrs={'rows': 3, 'class': 'textarea textarea_bordered h-24 w-full'}),
            'nexts': forms.Textarea(attrs={'rows': 3, 'class': 'textarea textarea_bordered h-24 w-full'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 初期値に今日の日付を設定する
        today = date.today()
        if not self.initial.get('report_date'):
               self.initial['on_date'] = today
        
        last_report = Report.objects.latest('on_date')
        if last_report.on_date.isocalendar()[:2] == today.isocalendar()[:2]:
              self.initial['weekly_target'] = last_report.weekly_target