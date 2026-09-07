# # Import necessary modules
# from flask import render_template, request, make_response
# from app import app
# from app.models.user import User
# from flask_login import login_required
# import csv
# from io import StringIO

# # Define a route for viewing registered users
# @app.route('/view_registered_users', methods=['GET'])
# @login_required  # Use login_required to ensure only logged-in admins can access this page
# def view_registered_users():

#     # Get search query from the request
#     branch_query = request.args.get('branch', '').strip()
#     gender_query = request.args.get('gender', '').strip()
#     category_query = request.args.get('category', '').strip()
    

#     # Query the database for registered users
#     users_query = User.query

#     if branch_query:
#         users_query = users_query.filter(User.branch.ilike(f'%{branch_query}%'))

#     if gender_query:
#         users_query = users_query.filter(User.gender.ilike(f'%{gender_query}%'))
    
#     if category_query:
#         users_query = users_query.filter(User.category.ilike(f'%{category_query}%'))


#         # Paginate the results
#         page = request.args.get('page', 1, type=int)
#         registered_users = users_query.paginate(page=page, per_page=10)

#     # Retrieve the page number from the request, default to 1 if not provided
#     page = request.args.get('page', default=1, type=int)

#     # Set the number of results per page
#     per_page = 10  # You can adjust this to your desired number of results per page

#     # Query registered users with pagination
#     registered_users = User.query.paginate(page=page, per_page=per_page, error_out=False)

#     return render_template('admin/view_registered_users.html', registered_users=registered_users, branch_query=branch_query,
#         gender_query=gender_query, category_query=category_query)

# @app.route('/download_registered_users', methods=['GET'])
# def download_registered_users():
#     # Get filter criteria from the request
#     branch_query = request.args.get('branch', '').strip()
#     gender_query = request.args.get('gender', '').strip()
#     category_query = request.args.get('category', '').strip()

#     # Base query
#     users_query = User.query

#     # Apply filters
#     if branch_query:
#         users_query = users_query.filter(User.branch.ilike(f'%{branch_query}%'))
#     if gender_query:
#         users_query = users_query.filter(User.gender.ilike(f'%{gender_query}%'))
#     if category_query:
#         users_query = users_query.filter(User.category.ilike(f'%{category_query}%'))

#     # Fetch all filtered users
#     users = users_query.all()

#     # Create CSV data
#     csv_data = StringIO()
#     writer = csv.writer(csv_data)
#     writer.writerow(['Name', 'Email', 'Phone Number', 'Branch', 'Gender', 'Status', 'Category', 'Age Range', 'Payment Date', 'Expectations', 'Registration Pin'])

#     for user in users:
#         writer.writerow([
#             f"{user.first_name} {user.last_name}",
#             user.email,
#             user.number,
#             user.branch,
#             user.gender,
#             user.marital_status,
#             user.category,
#             user.age_range,
#             user.payment_date,
#             user.expectations,
#             user.registration_pin,
#         ])

#     # Prepare the response
#     response = make_response(csv_data.getvalue())
#     response.headers['Content-Disposition'] = 'attachment; filename=registered_users.csv'
#     response.headers['Content-Type'] = 'text/csv'

#     return response