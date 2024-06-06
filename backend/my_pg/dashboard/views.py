# from django.shortcuts import render

# Create your views here.
from django.db.models import Avg
from datetime import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from tenants.models import Tenant
from payments.models import Payment
from facilities.models import FacilityBooking
from complaints.models import Complaint
from expenses.models import Expense
from django.db.models import Sum, Count

class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Tenant Summary
        total_tenants = Tenant.objects.count()
        occupied_rooms = Tenant.objects.filter(is_active=True).count()
        total_rooms = total_tenants  # Assuming each tenant occupies one room
        occupancy_rate = (occupied_rooms / total_rooms) * 100 if total_rooms else 0
        upcoming_move_ins = Tenant.objects.filter(move_in_date__gt=timezone.now()).count()
        upcoming_move_outs = Tenant.objects.filter(move_out_date__gt=timezone.now()).count()
        tenant_summary = {
            'totalTenants': total_tenants,
            'occupancyRate': occupancy_rate,
            'upcomingMoveIns': upcoming_move_ins,
            'upcomingMoveOuts': upcoming_move_outs,
        }

        # Financial Overview
        total_revenue = Payment.objects.aggregate(Sum('amount'))['amount__sum'] or 0
        total_expenses = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0
        profit_loss = total_revenue - total_expenses
        pending_payments = Payment.objects.filter(status='pending').count()
        overdue_payments = Payment.objects.filter(status='overdue').count()
        financial_overview = {
            'totalRevenue': total_revenue,
            'totalExpenses': total_expenses,
            'profitLoss': profit_loss,
            'pendingPayments': pending_payments,
            'overduePayments': overdue_payments,
        }

        # Facility Utilization
        booking_status = FacilityBooking.objects.filter(status='booked').count()
        total_facilities = FacilityBooking.objects.count()
        utilization_rate = (booking_status / total_facilities) * 100 if total_facilities else 0
        popular_facilities = FacilityBooking.objects.values('facility').annotate(count=Count('facility')).order_by('-count')[:5]
        popular_facilities = [facility['facility'] for facility in popular_facilities]
        upcoming_bookings = FacilityBooking.objects.filter(booking_date__gt=timezone.now()).count()
        facility_utilization = {
            'bookingStatus': booking_status,
            'utilizationRate': utilization_rate,
            'popularFacilities': popular_facilities,
            'upcomingBookings': upcoming_bookings,
        }

        # Complaint Analysis
        total_complaints = Complaint.objects.count()
        unresolved_complaints = Complaint.objects.filter(status='unresolved').count()
        complaint_categories = Complaint.objects.values('category').annotate(count=Count('category')).order_by('-count')
        complaint_categories = [category['category'] for category in complaint_categories]
        average_resolution_time = Complaint.objects.aggregate(Avg('resolution_time'))['resolution_time__avg'] or 0
        complaint_analysis = {
            'totalComplaints': total_complaints,
            'unresolvedComplaints': unresolved_complaints,
            'complaintCategories': complaint_categories,
            'averageResolutionTime': average_resolution_time,
        }

        return Response({
            'tenantSummary': tenant_summary,
            'financialOverview': financial_overview,
            'facilityUtilization': facility_utilization,
            'complaintAnalysis': complaint_analysis,
        })
