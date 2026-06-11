Project Setup :
------------------
-> Create a virtual Environment in base dir and activate it
    pip install pipenv

-> Install these Libraries in the virtual Envirnment created
    pipenv install django
    pipenv install python-dotenv
    pipenv install djangorestframework
    pipenv install reportlab

-------------------
Current Progress :
-------------------
-> For Users 
    Register/Login
    Can search, check price & explore any adventure
    filter them using Categories (Indoor, Outdoor & Events)
    Book tickets for any events (Tickets generates automatically using reportlab & send to mail)
    A booking tab where user can see their previous bookings


-> For Vendor
    Register/Login
    Create an adventure (Promote their Event/Place)
    Set Price & Main image(Thumbnail) of adventure
    Can edit the adventure later


------------------
To Be Done : 
------------------
-> For Users :
    Takes location from user and how the result near or close to them first
    Add section to include few images of the place(adventure)
    Comment and Rating Feature
    Add a section to customise user profile
    Payment Integration


-> For Vendor
    Build Working Stats Function to show number of booking and revenue generated within a time span (For Both Overall Adventures & Seperate Adventures)

-> For Admin/Selected Users 
    Verification feature to verify if the adventure added by user is safe & authorized.
