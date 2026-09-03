from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.http import HttpResponse

from openpyxl import Workbook

from .models import Student
from .forms import StudentForm


# ============================================================
# DASHBOARD
# ============================================================

def dashboard(request):

    total_students = Student.objects.count()

    # Course statistics
    course_stats = (
        Student.objects
        .values("course")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    # Experience statistics
    fresher_count = Student.objects.filter(
        experience_fresher__icontains="fresher"
    ).count()

    experienced_count = Student.objects.filter(
        experience_fresher__icontains="experienced"
    ).count()

    recent_students = Student.objects.order_by("-id")[:10]

    context = {
        "total_students": total_students,
        "course_stats": course_stats,
        "fresher_count": fresher_count,
        "experienced_count": experienced_count,
        "recent_students": recent_students,
    }

    return render(
        request,
        "students/dashboard.html",
        context
    )


# ============================================================
# CREATE STUDENT
# ============================================================

def student_create(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():

            student = form.save()

            messages.success(
                request,
                f"Student '{student.name}' registered successfully!"
            )

            return redirect("student_list")

    else:
        form = StudentForm()

    context = {
        "form": form,
        "title": "Register Student",
        "button_text": "Register Student",
    }

    return render(
        request,
        "students/student_form.html",
        context
    )


# ============================================================
# READ / LIST STUDENTS
# ============================================================

def student_list(request):

    search = request.GET.get("search", "").strip()

    students = Student.objects.all().order_by("-id")

    if search:

        students = students.filter(
            Q(name__icontains=search) |
            Q(mobile_no__icontains=search) |
            Q(email_id__icontains=search) |
            Q(course__icontains=search)
        )

    paginator = Paginator(students, 10)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    context = {
        "students": page_obj,
        "search": search,
        "page_obj": page_obj,
    }

    return render(
        request,
        "students/student_list.html",
        context
    )


# ============================================================
# STUDENT DETAILS
# ============================================================

def student_detail(request, pk):

    student = get_object_or_404(
        Student,
        pk=pk
    )

    context = {
        "student": student
    }

    return render(
        request,
        "students/student_detail.html",
        context
    )


# ============================================================
# UPDATE STUDENT
# ============================================================

def student_update(request, pk):

    student = get_object_or_404(
        Student,
        pk=pk
    )

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():

            student = form.save()

            messages.success(
                request,
                f"Student '{student.name}' updated successfully!"
            )

            return redirect(
                "student_detail",
                pk=student.pk
            )

    else:

        form = StudentForm(
            instance=student
        )

    context = {
        "form": form,
        "student": student,
        "title": "Edit Student",
        "button_text": "Update Student",
    }

    return render(
        request,
        "students/student_form.html",
        context
    )


# ============================================================
# DELETE STUDENT
# ============================================================

def student_delete(request, pk):

    student = get_object_or_404(
        Student,
        pk=pk
    )

    if request.method == "POST":

        student_name = student.name

        student.delete()

        messages.success(
            request,
            f"Student '{student_name}' deleted successfully!"
        )

        return redirect("student_list")

    context = {
        "student": student
    }

    return render(
        request,
        "students/student_confirm_delete.html",
        context
    )


# ============================================================
# EXPORT TO EXCEL
# ============================================================

def export_students_excel(request):

    students = Student.objects.all().order_by("-id")

    workbook = Workbook()

    worksheet = workbook.active

    worksheet.title = "Students"

    headers = [
        "ID",
        "Date",
        "Name",
        "Mobile No",
        "Alternate No",
        "Email",
        "Address",
        "Course",
        "Batch",
        "Experience/Fresher",
        "How You Know",
        "Contact",
        "Counselor",
        "Fees",
        "Comment",
        "Selected Type",
    ]

    worksheet.append(headers)

    for student in students:

        worksheet.append([
            student.id,
            student.date,
            student.name,
            student.mobile_no,
            student.alternate_no,
            student.email_id,
            student.address,
            student.course,
            student.batch,
            student.experience_fresher,
            student.how_you_know,
            student.contact,
            student.counselor,
            student.fees,
            student.comment,
            student.selected_type,
        ])

    # Adjust column widths

    for column in worksheet.columns:

        max_length = 0

        column_letter = column[0].column_letter

        for cell in column:

            if cell.value is not None:

                cell_length = len(str(cell.value))

                if cell_length > max_length:
                    max_length = cell_length

        worksheet.column_dimensions[
            column_letter
        ].width = min(max_length + 2, 40)

    response = HttpResponse(
        content_type=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        )
    )

    response["Content-Disposition"] = (
        'attachment; filename="students.xlsx"'
    )

    workbook.save(response)

    return response