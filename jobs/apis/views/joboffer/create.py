from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from users.permissions import UserActive
from varieties.models import Currency, City, Country
from memberships.models import AdMembership, UserMembership
from globals.payment_helpers import create_charge, create_customer
from globals.global_tasks import reward_user
from globals.ad_helpers import update_ad_type
from jobs.models import JobOffer, ExperienceLevel, ContractType, Grade, JobSector, JobTitle, Benefit


def create_joboffer(user, title, job_sector, description, country_model, city_model, currency_model, salary, phone_number, contract_type_model, working_days, work_from_home, shift_system, grade_model, exp_level_model, require_vehicle, require_license, gender):
    ad = JobOffer.objects.create(
        user=user,
        job_title=title,
        job_description=description,
        country=country_model,
        city=city_model,
        currency=currency_model,
        salary=salary,
        phone_number=phone_number,
        contract_type=contract_type_model,
        working_days=working_days,
        work_from_home=work_from_home,
        require_license=require_license,
        require_vehicle=require_vehicle,
        shift_system=shift_system,
        grade=grade_model,
        exp_level=exp_level_model,
        gender=gender,
        job_sector=job_sector
    )
    return ad

def add_benefits(ad, benefits):
    benefits_list = []
    for benefit in benefits:
        benefit_model = Benefit.objects.create(
            name = benefit
        )
        benefits_list.append(benefit_model)
    ad.benefits.set(benefits_list)



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
    job_title = data.get("sector")
    job_sector = data.get("title")
    job_description = data.get("description")
    country = data.get("country")
    city = data.get("city")
    currency = data.get("currency")
    salary = data.get("salary")
    phone_number = data.get("phone_number")
    contract_type = data.get("contract_type")
    working_days = data.get("working_days")
    work_from_home = data.get("work_from_home")
    require_license = data.get("require_license")
    require_vehicle = data.get("require_vehicle")
    shift_system = data.get("shift_system")
    grade = data.get("grade")
    exp_level = data.get("exp_level")
    gender = data.get("gender")
    membership_name = data.get("membership_name")
    benefits = data.get("benefits")


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

    if not job_description:
        return Response({
            "message": "Please enter description"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not salary:
        return Response({
            "message": "Please enter salary"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not gender:
        return Response({
            "message": "Please enter gender"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not work_from_home:
        return Response({
            "message": "Please specify if it's available to work from home"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not require_license:
        return Response({
            "message": "Please specify if it's required to have a drive license"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not require_vehicle:
        return Response({
            "message": "Please specify if it's required to have a vehicle"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not working_days:
        return Response({
            "message": "Please enter working days"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not currency:
        return Response({
            "message": "Please enter currency"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        currency_model = Currency.objects.get(name=currency)
    except Currency.DoesNotExist:
        return Response({
            "message": "this currency doesn't exists"
        }, status=status.HTTP_404_NOT_FOUND)

    if not country:
        return Response({
            "message": "Please enter country"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        country_model = Country.objects.get(name=country)
    except Country.DoesNotExist:
        return Response({
            "message": "There's no country with this name"
        }, status=status.HTTP_404_NOT_FOUND)

    if not city:
        return Response({
            "message": "Please enter city"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        city_model = City.objects.get(name=city)
    except City.DoesNotExist:
        return Response({
            "message": "There's no city with this name"
        }, status=status.HTTP_404_NOT_FOUND)

    if not contract_type:
        return Response({
            "message": "Please enter contract type"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        contract_type_model = ContractType.objects.get(name=contract_type)
    except ContractType.DoesNotExist:
        return Response({
            "message": "There's no contract type with this name"
        }, status=status.HTTP_404_NOT_FOUND)

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
            ad = create_joboffer(
                user=user,
                currency_model=currency_model,
                title=job_title_model,
                description=job_description,
                country_model=country_model,
                city_model=city_model,
                salary=salary,
                phone_number=phone_number,
                grade_model=grade_model,
                contract_type_model=contract_type_model,
                work_from_home=work_from_home,
                working_days=working_days,
                shift_system=shift_system,
                require_license=require_license,
                require_vehicle=require_vehicle,
                exp_level_model=exp_level_model,
                job_sector=job_sector_model
                )
            add_benefits(ad, benefits)
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
            ad = create_joboffer(
                user=user,
                currency_model=currency_model,
                title=job_title_model,
                description=job_description,
                country_model=country_model,
                city_model=city_model,
                salary=salary,
                phone_number=phone_number,
                grade_model=grade_model,
                contract_type_model=contract_type_model,
                work_from_home=work_from_home,
                working_days=working_days,
                shift_system=shift_system,
                require_license=require_license,
                require_vehicle=require_vehicle,
                exp_level_model=exp_level_model,
                job_sector=job_sector_model
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
            ad = create_joboffer(
                user=user,
                currency_model=currency_model,
                title=job_title_model,
                description=job_description,
                country_model=country_model,
                city_model=city_model,
                salary=salary,
                phone_number=phone_number,
                grade_model=grade_model,
                contract_type_model=contract_type_model,
                work_from_home=work_from_home,
                working_days=working_days,
                shift_system=shift_system,
                require_license=require_license,
                require_vehicle=require_vehicle,
                exp_level_model=exp_level_model,
                job_sector=job_sector_model
                )
            return Response({
                "message": "Congratulations! your ad is available now!"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                "message": "an error occurred while publishing your ad, please try again"
            }, status=status.HTTP_400_BAD_REQUEST)
