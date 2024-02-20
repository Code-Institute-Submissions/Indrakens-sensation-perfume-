# TABLE OF CONTENT

## MANUAL TESTING
### Account Registration
|  TEST                                                  | RESULTS  |
|---------|--------:|
| User can create an account                             |  PASS  |
| User receives email verification                       |  PASS  |
| User can click on Login link - redirects to Login page |  PASS  |  
| User can click on Home link - redirects to Home page   |  PASS  | 
### Account Login
|  TEST                                                                                                    |  RESULTS  |
|---------|---------:|
| User can log-in                                                                                          |  PASS  |
| User is notified of logging in to account                                                                |  PASS  |
| User can save login details                                                                              |  PASS  |
| User can click on Register link - redirects to Register page                                             |  PASS  |
| User can click on Home link - redirects to Home page                                                     |  PASS  |
| User can click on Forgot Pasword link - redirects to pasword reset page, pasword reset sent to user email|  PASS  |
| User can click on link sent in email to reset pasword - redirects to web Change Pasword                  |  PASS  |
| User can change pasword - notifie pasword change                                                         |  PASS  |
### Accoun Logout
| User can log-out - redirects to Log out page        |  PASS |
| User can click on Home link - redirects to home page|  PASS |
| User is notified of logging out of account          |  PASS |   
### Navigation - Logout/ Not Registered User
|     TEST                                                                                                   | RESULTS  |
|---------|--------:|
| User can click on Shop All and navigate to - categories, price, shop all                                   |  PASS  |
| User can click on For Her and navigate to - eau de parfum, eau de toilette, all for her                    |  PASS  |
| User can click on For Him and navigate to - eau de parfum, eau de toilette, all for him                    |  PASS  |
| User can click on Gift Sets and navigate to - gift sets for her, gift sets for him, all gift sets          |  PASS  |
| User can click on Sales and navigate to - for her, gift sets for her, for him, gift sets for him, all sales|  PASS  |
| User can click on Blog and navigate to - Sensation-Perfume-Blog                                            |  PASS  |
| User navigate to Sensation-Perfume-Blog detail page                                                        |  PASS  | 
| User can click on Shopping bag and navigate to - shopping bag                                              |  PASS  |
| User can click on Login/ Sign Up and navigate to - register, login                                         |  PASS  |
| User can navigate to product page                                                                          |  PASS  |
| User can navigate to product detail page                                                                   |  PASS  |
### Navigation - Login/ Registered User
|     TEST                                                                                                   | RESULTS  |
|---------|--------:|
| User can click on Shop All and navigate to - categories, price, shop all                                   |  PASS  |
| User can click on For Her and navigate to - eau de parfum, eau de toilette, all for her                    |  PASS  |
| User can click on For Him and navigate to - eau de parfum, eau de toilette, all for him                    |  PASS  |
| User can click on Gift Sets and navigate to - gift sets for her, gift sets for him, all gift sets          |  PASS  |
| User can click on Sales and navigate to - for her, gift sets for her, for him, gift sets for him, all sales|  PASS  |
| User can click on Blog and navigate to - Sensation-Perfume-Blog                                            |  PASS  |
| User navigate to Sensation-Perfume-Blog detail page                                                        |  PASS  | 
| User can click on Shopping bag and navigate to - shopping bag                                              |  PASS  |
| User can click on Username- Profile and navigate to - username-profile, logout                             |  PASS  |
| User can navigate to product page                                                                          |  PASS  |
| User can navigate to product detail page                                                                   |  PASS  |
### Product Sorting and Searching
|   TEST                                                                               |  RESULTS |
|--------|---------:|
| User can click on search field and search for a product by - name, description       |  PASS |
| User can click on Sort by in product pages and sort products by - price (low to high)|  PASS | 
| User can click on Sort by in product pages and sort products by - price (high to low)|  PASS | 
| User can click on Sort by in product pages and sort products by - name (A to Z)      |  PASS | 
| User can click on Sort by in product pages and sort products by - name (Z to A)      |  PASS | 
| User can click on Sort by in product pages and sort products by - category (A to Z)  |  PASS |
| User can click on Sort by in product pages and sort products by - category (Z to A)  |  PASS | 
### Product Detail Page
|  TEST                                                                                                                           |  RESULTS |
|--------|---------:| 
| User can choose to add gift wrap to product by clicking on Offer Gift Wrap - Includes Gift Bag & Decorative Ribbon (if provided)| PASS |
| User can add product quantity                                                                                                   | PASS |
| User can click on Keep Shopping button - redirects to all product page                                                          | PASS |
| User can click on Add To Bag button - notifies added product in shopping bag                                                    | PASS |
### Shopping Bag
|   TEST                                                                   |  RESULTS |
|--------|--------:|
| User can update product quantity - notifies updated product quantity     | PASS |
| User can click on Keep Shopping button - redirects to all product page   | PASS |
| User can click on Go To Checkout button - redirects to checkout page     | PASS |
| User can remove product from shopping bag - notifies removed product     | PASS |
### Checkout - Not Login/ Registered User
|    TEST                                                                                                  |  RESULT |
|-----------|----------:|
| User can  easily fill the form to complete the order                                                     |  PASS |
| User can easily add card payment                                                                         |  PASS |
| User can click on Adjust Bag button - redirects to shopping bag                                          |  PASS |
| User can click on Complete Order button - redirects to order confirmation page and notifies order number |  PASS |
| User can click on Check Out The Latest Sales in order confirmation page - redirects to All Sales page    |  PASS |
### Checkout - Login User
|    TEST                                                                                                  |  RESULT |
|-----------|----------:|
| User can  easily fill the form to complete the order                                                     |  PASS |
| User can easily add card payment                                                                         |  PASS |
| User can save delivery information to profile                                                            |  PASS |
| User can click on Adjust Bag button - redirects to shopping bag                                          |  PASS |
| User can click on Complete Order button - redirects to order confirmation page and notifies order number |  PASS |
| User order information saved in user profile Order History                                               |  PASS |
| User can click on Check Out The Latest Sales in order confirmation page - redirects to All Sales page    |  PASS |
### User Profile
|    TEST                                                                                                                                                     |  RESULTS |
|--------|--------:|
| User can view delivery information and order history                                                                                                        |  PASS |
| User can click on order number in order history and view past order confirmation - redirects to order confirmation page and notifies past order confirmation|  PASS |
| User can click on Back To Profile button - redirects to user profile page                                                                                   |  PASS |
| User can click on Home link - redirects to home page                                                                                                        |  PASS |
| User can click on Update Profile button - redirects to Update user Profile page                                                                             |  PASS |
### Update User Profile
|    TEST                                                                                                                                                     |  RESULTS |
|--------|--------:|
| User can update delivery information - notifies updated profile and redirects to profile page                                                               |  PASS |
| User can add, update, remove profile picture - notifies updated profile and redirects to profile page                                                       |  PASS |
| User can click on order number in order history and view past order confirmation - redirects to order confirmation page and notifies past order confirmation|  PASS |
| User can delete order history order number - redirects to profile page and notifies deleted order number from order history                                 |  PASS |
| User can click on Cancel link - redirects to profile page                                                                                                   |  PASS |
### Blog - Not Login/ Registered User
|   TEST                                                            |  RESULTS  |
|----------|-----------:|
| User can click on blog - redirects to Sensation-Perfume Blog page |  PASS |
| User can click on post title - redirects to blog post detail page |  PASS |
### Blog - Login User
|   TEST                                                            |  RESULTS  |
|-------|---------:|
| User can click on blog - redirects to Sensation-Perfume Blog page |  PASS |
| User can click on post title - redirects to blog post detail page |  PASS |
| User can like/ unlike post                                        |  PASS |
| User can leave comment in blog post - notifies posted comment     |  PASS |
### Subscribe
|  TEST      | RESULTS |
|--------|-------:|
| User can subscribe to newslwtter - notifies subscribing | PASS |
| Notification | <img width="818" alt="Screenshot 2024-02-20 175748" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/f1641f8a-bc6d-483e-9518-ec9744751abd">|
| Subscribed User email in Mailchimp (not login and login user) | <img width="959" alt="Screenshot 2024-02-20 182414" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/4c2ffbc9-4bde-4aa2-9efe-45ced68d7f4e">|
### Social Links
|  TESTS                                                                        | RESULTS |
|-------|-------:|
| User can click on Twitter icon - redirects to twiter.com page                  | PASS |
| User can click on Instagram icon - redirects to instagram.com page             | PASS |
| User can click on Facebook icon - redirects to Sensation Perfume facebook page | PASS |
| Sensation Perfume Facebook page | <img width="956" alt="Screenshot 2024-02-20 181804" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/4dc131ae-4c4d-49c5-bb7c-c4fe37a2bfec">|
### Super User 
|  TEST                                                                                                                                   |  RESULTS |
|--------|---------:|
| Super user can login in admin panel                                                                                                     |  PASS  |
| Super User can update product in product detail page - redirects to Profile management update product page and notifies updating product|  PASS  | 
| Super User can add product by clicking on Username-Profile Product Management - redirects to Profile Managemente Add Product            |  PASS  |
| Super User can delete product in product detail page - redirects to all product page and notifies deleted product                       |  PASS  |

## CI PYTHON LINTER [pep8ci](https://pep8ci.herokuapp.com/)
|     |      |
|-----|------|
| sensation/ urls.py | <img width="521" alt="Screenshot 2024-02-19 202309" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/216fa09a-affb-4efd-aa85-18af4fcd9b97">|
| sensation/ views.py | <img width="526" alt="Screenshot 2024-02-19 202959" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/96a12df3-988c-4046-a792-6b1528674885"> |
| sensation/ wsgi.py | <img width="507" alt="Screenshot 2024-02-19 203549" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/64c668ec-9b75-4dd9-ab5e-c8010c641e60"> |
| sensation/ asgi.py | <img width="505" alt="Screenshot 2024-02-19 203838" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/b69d8055-4a82-4ac3-8e0b-ea98442e1c02"> |
#
|      |        |
|------|-------|
| home/ views.py | <img width="515" alt="Screenshot 2024-02-19 204414" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/c8b1fda1-b292-4d77-badc-5643d7acaf75">|
| home/ urls.py | <img width="519" alt="Screenshot 2024-02-19 204604" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/fc5c29b8-5396-4ea8-940f-3a8e4bbde437"> |
#
|      |       |
|------|--------|
| blog/ views.py | <img width="521" alt="Screenshot 2024-02-19 205858" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/c704a3fd-a80b-4a56-a806-e2c1b4ddc7cd">|
| blog/ urls.py | <img width="513" alt="Screenshot 2024-02-19 210149" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/f11d994e-21d4-4b41-b764-267b9988bb3a">|
| blog/ models.py | <img width="528" alt="Screenshot 2024-02-19 210950" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/82d7100a-2fa3-49e0-bcac-09f925763e38">|
| blog/ admin.py | <img width="518" alt="Screenshot 2024-02-19 211352" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/ed53ab55-f01f-459e-bc69-36a03f960b9c"> |
#
|     |      |
|----|-----|
| bag/ views.py | <img width="578" alt="Screenshot 2024-02-20 003255" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/6a8f5f79-96a0-45ea-ac08-130fd6d6741e">|
| bag/ urls.py | <img width="534" alt="Screenshot 2024-02-19 214722" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/e127fb06-cfbf-47ca-895f-ce08a9e4d76d">|
| bag/ context.py | <img width="538" alt="Screenshot 2024-02-19 220419" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/29788c2e-8746-454e-bdcd-285b1b206c5d">|
| bag/ shopping_bag_tools.py| <img width="534" alt="Screenshot 2024-02-19 220753" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/d6dcff6b-ca35-431b-bb57-1f150023e57a">|
#
|      |    |
|-----|-----|
| checkout/ webhooks.py | <img width="552" alt="Screenshot 2024-02-19 221316" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/6146bdf6-aa35-4e76-b45d-0f31e080c635">|
| checkout/ views.py | <img width="517" alt="Screenshot 2024-02-19 230449" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/24493623-a4f7-42d4-97df-43fcdc2176a6">|
| checkout/ urls.py | <img width="553" alt="Screenshot 2024-02-19 230758" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/b75d1b31-fc0f-47e2-aff5-277308d4a979">|
| checkout/ signals.py | <img width="540" alt="Screenshot 2024-02-19 230948" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/dc39c120-51b3-4ffa-8823-887125131863">|
| checkout/ models.py | <img width="551" alt="Screenshot 2024-02-19 232050" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/7726e6ba-135b-4436-9280-2bfd3db0d4b1">|
| checkout/ forms.py | <img width="534" alt="Screenshot 2024-02-19 232327" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/f5867d38-3d9d-45e0-8c3f-d0c24a91adc8">|
| checkoit/ admin.py | <img width="534" alt="Screenshot 2024-02-19 232527" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/0b0900dc-45e4-4aac-95c9-e19ea7089f0d">|  
#
|     |      |
|-----|------|
| products/ views.py | <img width="539" alt="Screenshot 2024-02-19 233850" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/9a99ec90-6529-47bb-bfbf-928d42f99276">|
| products/ urls.py | <img width="510" alt="Screenshot 2024-02-19 234200" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/627c24a9-28cc-46ac-9c9a-accdf33cf7a7">|
| products/ models.py | <img width="512" alt="Screenshot 2024-02-19 234913" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/0e6578b0-0054-44d7-9d56-aeabe26018e6">|
| products/ forms.py | <img width="527" alt="Screenshot 2024-02-19 235107" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/6b112f7d-2484-4a9c-8cc0-9f2601586f0e">|
| products/ admin.py | <img width="556" alt="Screenshot 2024-02-19 235416" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/beccda8b-b141-41ce-b340-953b0ba8e461">|
#
|   |    |
|----|----|
| profiles/ views.py | <img width="547" alt="Screenshot 2024-02-19 235829" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/8c45f0e6-416c-4794-b64c-00c411d2d81c">|
| profiles/ urls.py | <img width="548" alt="Screenshot 2024-02-20 000127" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/787e7dbc-33d0-4a11-ac28-d0ccc237c9f6">|
| profiles/ models.py | <img width="519" alt="Screenshot 2024-02-20 000929" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/a023a502-b747-4508-beb8-2bba9b5fabc9">|
| profiles/ forms.py | <img width="556" alt="Screenshot 2024-02-20 001107" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/fcc88f88-b30d-47b5-bfc7-b1891c7b8bbd">|
## HTML VALIDATION
Due to the Django codes in templates, [W3C Markup Validation Service](https://validator.w3.org/) shows errors, for that reason only included base.html validator result
|      |      |
|------|------|
| Result | <img width="894" alt="Screenshot 2024-02-20 004832" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/d32ee635-1217-43e4-9509-99a6078c537c">|
|  Result | <img width="645" alt="Screenshot 2024-02-20 004939" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/6ced7a4b-732d-46d3-9af2-37a40e4de0c1">|
## CSS VALIDATION - [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
|      |      |
|------|-------|
| base.css| <img width="764" alt="Screenshot 2024-02-20 005856" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/c660d4f6-abd6-4dff-8935-7c47ed415086">|
| warnings | <img width="818" alt="Screenshot 2024-02-20 005911" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/bb337ef8-c3cd-4f27-ac70-d45bf7735d00">|
#
|     |      |
|------|------|
| user_profiles.css | <img width="766" alt="Screenshot 2024-02-20 010452" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/51d368dc-8f8f-4743-96be-284a9e053552">|
#
|      |      |
|-----|-------|
| order_checkout.css | <img width="769" alt="Screenshot 2024-02-20 011049" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/3c313559-6eb1-42f9-99ff-2576d1269393">|
| warnings | <img width="374" alt="Screenshot 2024-02-20 011105" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/0b657cc4-3460-4ef8-b6fe-bf25fab9524b">|
#
|      |      |
|-----|-------|
| blog.css | <img width="762" alt="Screenshot 2024-02-20 011457" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/5ef39474-d13f-4f94-843d-6a75d75c3f3c">|
## JAVASCRIPT - [JSHint](https://jshint.com/)
|       |        |
|-------|--------|
| country_field.js | <img width="957" alt="Screenshot 2024-02-20 013231" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/b2000947-c379-49f0-b90d-b41051a25632">|
| back to top click function| <img width="949" alt="Screenshot 2024-02-20 015107" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/98f9b31f-2ab7-46b0-89aa-8f70d7d96f54">|
| sort selector | <img width="952" alt="Screenshot 2024-02-20 020513" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/fc71e3fc-58f8-4a17-8fbd-f929eb155125">|
## GOOGLE LIGHTHOUSE
|       |       |
|------|-------|
| Lighthouse testing | <img width="575" alt="Screenshot 2024-02-20 022410" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/44ba4908-21b6-478e-b15c-52a15cc1630d">|
