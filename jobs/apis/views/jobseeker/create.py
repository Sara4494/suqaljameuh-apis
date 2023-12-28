from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from users.permissions import UserActive
from varieties.models import Currency, City, Country
from memberships.models import AdMembership, UserMembership
from globals.payment_helpers import create_charge, create_customer
from globals.global_tasks import reward_user
from globals.ad_helpers import update_ad_type
from jobs.models import JobSeeker, ExperienceLevel, ContractType, Grade, JobTitle, JobSector, Language, PreviousExp, PreviousCourse


def create_jobseeker(user, title, can_shift, salary, phone_number, full_name, contract_type_model, work_from_home, grade_model, exp_level_model, has_vehicle, has_license, gender, bio, job_sector, nationality, residence_country, residence_city, social_status, ready_status, working_hours, language, age, prev_exp, prev_course, cv):
    ad = JobSeeker.objects.create(
        user=user,
        full_name=full_name,
        phone_number=phone_number,
        bio=bio,
        job_title=title,
        job_sector=job_sector,
        nationality=nationality,
        residence_country=residence_country,
        residence_city=residence_city,
        can_shift=can_shift,
        contract_type=contract_type_model,
        gender=gender,
        social_status=social_status,
        ready_status=ready_status,
        age=age,
        salary=salary,
        language=language,
        has_vehicle=has_vehicle,
        has_license=has_license,
        working_hours=working_hours,
        work_from_home=work_from_home,
        grade=grade_model,
        exp_level=exp_level_model,
        prev_exp=prev_exp,
        prev_course=prev_course,
        cv=cv,
    )
    return ad


@api_view(["POST"])
@permission_classes([UserActive])
def publish_ad(request):
    data = request.data
    user = request.user

    if not data or data == None:
        return Response({
            "message": "Please Provide the needed data to publish your ad!"
        }, status=status.HTTP_400_BAD_REQUEST)

    # * These data are mandatory, and mostly doesn't change over the time
    full_name = data.get("full_name")
    phone_number = data.get("phone_number")
    bio = data.get("bio")
    job_title = data.get("job_title")
    job_sector = data.get("job_sector")
    nationality = data.get("nationality")
    residence_country = data.get("residence_country")
    residence_city = data.get("residence_city")
    can_shift = data.get("can_shift")
    contract_type = data.get("contract_type")
    gender = data.get("gender")
    social_status = data.get("social_status")
    ready_status = data.get("ready_status")
    age = data.get("age")
    skills = data.get("skills")
    salary = data.get("salary")
    language = data.get("language")
    has_vehicle = data.get("has_vehicle")
    has_license = data.get("has_license")
    working_hours = data.get("working_hours")
    work_from_home = data.get("work_from_home")
    grade = data.get("grade")
    exp_level = data.get("exp_level")
    prev_exp = data.get("prev_exp")
    prev_course = data.get("prev_course")
    cv = data.get("cv")
    membership_name = data.get("membership_name")

    if not job_title:
        return Response({
            "message": "Please enter title"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        job_title_model = JobTitle.objects.get(name=job_title)
    except JobTitle.DoesNotExist:
        return Response({
            "message": "this job title doesn't exists"
        }, status=status.HTTP_404_NOT_FOUND)

    if not job_sector:
        return Response({
            "message": "Please enter the job sector"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        job_sector_model = JobSector.objects.get(name=job_sector)
    except JobSector.DoesNotExist:
        return Response({
            "message": "this job sector doesn't exists"
        }, status=status.HTTP_404_NOT_FOUND)

    if not nationality:
        return Response({
            "message": "Please enter your nationality"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        nationality_model = Country.objects.get(name=nationality)
    except Country.DoesNotExist:
        return Response({
            "message": "this nationality doesn't exists"
        }, status=status.HTTP_404_NOT_FOUND)

    if not residence_country:
        return Response({
            "message": "Please enter your residence country"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        residence_country_model = Country.objects.get(name=residence_country)
    except Country.DoesNotExist:
        return Response({
            "message": "this country doesn't exists"
        }, status=status.HTTP_404_NOT_FOUND)

    if not residence_city:
        return Response({
            "message": "Please enter your residence country"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        residence_city_model = City.objects.get(name=residence_city)
    except City.DoesNotExist:
        return Response({
            "message": "this city doesn't exists"
        }, status=status.HTTP_404_NOT_FOUND)

    if not language:
        return Response({
            "message": "Please enter your residence country"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        language_model = Language.objects.get(name=language)
    except Language.DoesNotExist:
        return Response({
            "message": "this city doesn't exists"
        }, status=status.HTTP_404_NOT_FOUND)

    if prev_exp:
        try:
            PreviousExp.objects.create(
                job_title=prev_exp.job_title,
                company_name=prev_exp.company_name,
                description=prev_exp.description,
                from_date=prev_exp.from_date,
                to_date=prev_exp.to_date,
                current=prev_exp.current
            )
        except Exception as e:
            return Response({
                "message": "an error occurred while generating your previous experience"
            }, status=status.HTTP_404_NOT_FOUND)

    if prev_course:
        try:
            PreviousCourse.objects.create(
                job_title=prev_course.course_title,
                company_name=prev_course.company_name,
                from_date=prev_course.from_date,
                to_date=prev_course.to_date,
            )
        except Exception as e:
            return Response({
                "message": "an error occurred while generating your previous courses"
            }, status=status.HTTP_404_NOT_FOUND)

    if not salary:
        return Response({
            "message": "Please enter salary"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not bio:
        return Response({
            "message": "Please enter bio"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not full_name:
        return Response({
            "message": "Please enter full name"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not gender:
        return Response({
            "message": "Please enter gender"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not work_from_home:
        return Response({
            "message": "Please specify if it's available to work from home"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not grade:
        return Response({
            "message": "Please enter a grade"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        grade_model = Grade.objects.get(name=grade)
    except Grade.DoesNotExist:
        return Response({
            "message": "There's no grade with this name"
        }, status=status.HTTP_404_NOT_FOUND)

    if not contract_type:
        return Response({
            "message": "Please enter a contract type"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        contract_type_model = ContractType.objects.get(name=contract_type)
    except ContractType.DoesNotExist:
        return Response({
            "message": "There's no contract type with this name"
        }, status=status.HTTP_404_NOT_FOUND)

    if not exp_level:
        return Response({
            "message": "Please enter a exp_level"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        exp_level_model = ExperienceLevel.objects.get(name=exp_level)
    except ExperienceLevel.DoesNotExist:
        return Response({
            "message": "There's no experience level with this name"
        }, status=status.HTTP_404_NOT_FOUND)

    user_membership = None
    try:
        user_membership = UserMembership.objects.get(subscriber=user)
    except UserMembership.DoesNotExist:
        pass

    # * if the user has a membership, we'll feature his Ad
    if user_membership != None:
        base_user_membership = user_membership.membership
        try:
            ad = create_jobseeker(
                user=user,
                job_title=job_title_model,
                job_sector=job_sector_model,
                residence_country=residence_country_model,
                residence_city=residence_city_model,
                salary=salary,
                phone_number=phone_number,
                full_name=full_name,
                contract_type=contract_type_model,
                work_from_home=work_from_home,
                has_license=has_license,
                has_vehicle=has_vehicle,
                grade=grade_model,
                exp_level=exp_level_model,
                gender=gender,
                prev_course=prev_course,
                prev_exp=prev_exp,
                can_shift=can_shift,
                bio=bio,
                ready_status=ready_status,
                age=age,
                language=language_model,
                working_hours=working_hours,
                cv=cv,
                nationality=nationality_model,
                social_status=social_status
            )
            update_ad_type(base_user_membership, ad)
            reward_user(user, ad)
            return Response({
                "message": "Congratulations! your ad has been featured and it's available now!"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                "message": "an error occurred while publishing your ad, please try again"
            }, status=status.HTTP_400_BAD_REQUEST)

    elif membership_name:
        stripe_token = data.get("stripe_token")
        try:
            membership = AdMembership.objects.get(name=membership_name)
        except AdMembership.DoesNotExist:
            return Response({
                "message": "There's no membership with this name!"
            }, status=status.HTTP_404_NOT_FOUND)

        try:
            customer = create_customer(user, stripe_token)
        except Exception as e:
            return Response({
                "message": "there's an error occurred while processing the payment, please try again"
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            create_charge(customer, membership.price,
                          description="Featuring Ad")
        except Exception as e:
            return Response({
                "message": "there's an error occurred while processing the payment, please try again"
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            ad = create_jobseeker(
                user=user,
                job_title=job_title_model,
                job_sector=job_sector_model,
                residence_country=residence_country_model,
                residence_city=residence_city_model,
                salary=salary,
                phone_number=phone_number,
                full_name=full_name,
                contract_type=contract_type_model,
                work_from_home=work_from_home,
                has_license=has_license,
                has_vehicle=has_vehicle,
                grade=grade_model,
                exp_level=exp_level_model,
                gender=gender,
                prev_course=prev_course,
                prev_exp=prev_exp,
                can_shift=can_shift,
                bio=bio,
                ready_status=ready_status,
                age=age,
                language=language_model,
                working_hours=working_hours,
                cv=cv,
                nationality=nationality_model,
                social_status=social_status
            )
            update_ad_type(membership, ad)
            reward_user(user, ad)
            return Response({
                "message": "Congratulations! your ad has been featured and it's available now!"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                "message": "an error occurred while publishing your ad, please try again"
            }, status=status.HTTP_400_BAD_REQUEST)

    else:
        try:
            ad = create_jobseeker(
                user=user,
                job_title=job_title_model,
                job_sector=job_sector_model,
                residence_country=residence_country_model,
                residence_city=residence_city_model,
                salary=salary,
                phone_number=phone_number,
                full_name=full_name,
                contract_type=contract_type_model,
                work_from_home=work_from_home,
                has_license=has_license,
                has_vehicle=has_vehicle,
                grade=grade_model,
                exp_level=exp_level_model,
                gender=gender,
                prev_course=prev_course,
                prev_exp=prev_exp,
                can_shift=can_shift,
                bio=bio,
                ready_status=ready_status,
                age=age,
                language=language_model,
                working_hours=working_hours,
                cv=cv,
                nationality=nationality_model,
                social_status=social_status
            )
            return Response({
                "message": "Congratulations! your ad is available now!"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                "message": "an error occurred while publishing your ad, please try again"
            }, status=status.HTTP_400_BAD_REQUEST)
