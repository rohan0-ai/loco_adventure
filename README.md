# Project Setup

1. Create a virtual environment in the project base directory and activate it.

```bash
pip install pipenv
```

2. Install the required libraries in the virtual environment.

```bash
pipenv install django
pipenv install python-dotenv
pipenv install djangorestframework
pipenv install reportlab
```

---

# Current Progress

## For Users

- Register/Login
- Search, check prices, and explore adventures
- Filter adventures using categories:
  - Indoor
  - Outdoor
  - Events
- Book tickets for events
  - Tickets are generated automatically using ReportLab
  - Tickets are sent via email
- View previous bookings from the **Bookings** section

## For Vendors

- Register/Login
- Create adventures (promote events or places)
- Set adventure price and thumbnail image
- Edit adventures after creation

---

# To Be Done

## For Users

- Use user location to prioritize nearby adventures
- Add support for multiple images for each adventure/place
- Comment and rating system
- User profile customization
- Payment gateway integration

## For Vendors

- Build a statistics dashboard showing:
  - Number of bookings
  - Revenue generated
  - Custom date-range filtering
  - Statistics for both overall and individual adventures

## For Admins / Verified Users

- Adventure verification system to ensure submitted adventures are safe, authentic, and authorized
