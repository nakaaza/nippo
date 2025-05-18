from collections import defaultdict
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Report
from .forms import ReportForm

def index(request):
	report_list = Report.objects.all().order_by('-on_date')
	weekly_groups = defaultdict(list)
	for item in report_list:
		week = item.on_date.isocalendar()[:2]
		weekly_groups[week].append(item)
	report_list_by_week = list(weekly_groups.values())
	form = ReportForm()
	context = {"report_list_by_week": report_list_by_week, 'form': form}
	return render(request, "reports/index.html", context)

def create(request):
	if request.method == 'POST':
		form = ReportForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("reports:index"))
		else:
			form = ReportForm()
	return render(request, reverse('reports:index'), {'form': form})
	
def detail(request):
	return "detail"