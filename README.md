# SENSATION - PERFUME 
<img width="796" alt="Screenshot 2024-02-17 195341" src="https://github.com/Indrakens/boutique_ado/assets/127971416/5f580240-73aa-4d82-8df0-29757ecfa767">
Sensation Perfume is an e-commerce website that sells perfumes for women and men. It has a payment type and subscription where users can subscribe for the latest sales and new product arrivals. 

Users can begin a shopping instance where they can select products they would like to buy from the database. When the user is done, they can be directed to their shopping bag to view what they have and they can either start the payment process, update/delete items, or go back to the products page and add more items. When the user completes their shopping process, they will receive an email confirming their order. Registered Users have access to the profile page where they can update profile details, upload images and delete order history.
#
Sensation Perfume uses the Django Python framework to generate views via HTML and CSS. JavaScript is used to handle posting user payments securely with Stripe. Javascript also was used for back-to-top button click functionality. All the pages are mainly styled with Bootstrap and custom CSS. All dependencies are handled by Pip.
#
The website was deployed via Heroku - the live site can be found here - 
[SENSATION - PERFUME](https://sensation-perfume-d52586ead80b.herokuapp.com/)
#
## TABLE OF CONTENT
* [UX](https://github.com/Indrakens/sensation-perfume/tree/main?tab=readme-ov-file#tehnology-used)
* [UX DESIGN](https://github.com/Indrakens/sensation-perfume/tree/main?tab=readme-ov-file#tehnology-used) 
   * [Color Scheme](https://github.com/Indrakens/sensation-perfume/tree/main?tab=readme-ov-file#color-scheme)
   * [Fonts](https://github.com/Indrakens/sensation-perfume/tree/main?tab=readme-ov-file#fonts)
   * [Images](https://github.com/Indrakens/sensation-perfume/tree/main?tab=readme-ov-file#images)
   * [Icons](https://github.com/Indrakens/sensation-perfume/tree/main?tab=readme-ov-file#icons) 
* [DATABASE MODEL](https://github.com/Indrakens/sensation-perfume/tree/main?tab=readme-ov-file#database)  
* [WIREFRAMES](https://github.com/Indrakens/sensation-perfume/tree/main?tab=readme-ov-file#wireframes)
   * [WEB](https://github.com/Indrakens/sensation-perfume/tree/main?tab=readme-ov-file#web)
   * [MOBILE](https://github.com/Indrakens/sensation-perfume/tree/main?tab=readme-ov-file#mobile)
* [BUSINESS MODEL](https://github.com/Indrakens/sensation-perfume/tree/main?tab=readme-ov-file#business-model)
* [SEO](https://github.com/Indrakens/sensation-perfume?tab=readme-ov-file#seo)
* [AGILE](https://github.com/Indrakens/sensation-perfume/tree/main?tab=readme-ov-file#agile) 
* [EPICS](https://github.com/Indrakens/sensation-perfume/tree/main?tab=readme-ov-file#epics)
* [USER STORIES](https://github.com/Indrakens/sensation-perfume/tree/main?tab=readme-ov-file#user-stories)
* [FEATURES](https://github.com/Indrakens/sensation-perfume/tree/main?tab=readme-ov-file#features)
   * [WEB](https://github.com/Indrakens/sensation-perfume/tree/main?tab=readme-ov-file#web)
   * [MOBILE](https://github.com/Indrakens/sensation-perfume/tree/main?tab=readme-ov-file#mobile)
* [FACEBOOK](https://github.com/Indrakens/sensation-perfume/tree/main?tab=readme-ov-file#facebook)    
* [TESTING](https://github.com/Indrakens/sensation-perfume/tree/main?tab=readme-ov-file#testing)
* [TEHNOLOGY USED](https://github.com/Indrakens/sensation-perfume/tree/main?tab=readme-ov-file#tehnology-used)
* [FEATURE TO IMPLEMENT](https://github.com/Indrakens/sensation-perfume?tab=readme-ov-file#feature-to-implement)
* [BUG](https://github.com/Indrakens/sensation-perfume?tab=readme-ov-file#bug)
* [DEPLOYMENT](https://github.com/Indrakens/sensation-perfume?tab=readme-ov-file#deployment)
* [FORKING AND CLONING](https://github.com/Indrakens/sensation-perfume?tab=readme-ov-file#forking-and-cloning)
  * [Forking The Repository](https://github.com/Indrakens/sensation-perfume?tab=readme-ov-file#forking-the-repository)
  * [Create A Clone Of Repository](https://github.com/Indrakens/sensation-perfume?tab=readme-ov-file#create-a-clone-of-repository)
* [CONTENT AND RESOURCES](https://github.com/Indrakens/sensation-perfume?tab=readme-ov-file#content-and-resources)  
* [ACKNOWLEDGMENT](https://github.com/Indrakens/sensation-perfume?tab=readme-ov-file#acknowledgment)
## UX
### UX DESIGN
#### Color Scheme 
|   |   |
|----|----|
|Color Palette [COOLORS](https://coolors.co/)| ![color palete sensation](https://github.com/Indrakens/sensation-perfume/assets/127971416/e4400906-312f-4e2b-a5ff-6e04cf176e9f)
|
#### Fonts
* The website uses ['LIVVIC'](https://fonts.google.com/?query=Livvic) and ['CINZEL DECORATIVE'](https://fonts.google.com/specimen/Cinzel+Decorative?query=Cinzel) fonts from [Google Fonts](https://fonts.google.com/) .
#### IMAGES
|   |   |
|----|----|
| Logo image was created in [CANVA](https://www.canva.com/)| ![22374AC2-DAB6-4E46-8EB2-5DF4B7A7E7CE](https://github.com/Indrakens/sensation-perfume/assets/127971416/ee9fbf46-aca5-45b3-a3b0-6a093b630b34)|
| Home page image was created in [CANVA](https://www.canva.com/)| ![90674E5C-AB18-45BE-8D23-E06C36CDF78A (2)](https://github.com/Indrakens/sensation-perfume/assets/127971416/4eaf2844-a701-40dc-988f-fb02ed4e8610)|
#### ICONS
* The website uses from [Font Awesome]( https://fontawesome.com/ ) icons.
## DATABASE
|         |        |
|---------|----------|
| Conceptual ERD | ![New Wireframe 1 (1)](https://github.com/Indrakens/sensation-perfume/assets/127971416/9ef098d8-c760-449b-b59a-35eb2d76a276)|
#
## WIREFRAMES
### WEB
|        |          |
|----------|----------|
| Home Page | ![home page](https://github.com/Indrakens/sensation-perfume/assets/127971416/5d36baa2-fd0c-4e69-b351-6dbbd107e03f)|
| Product Page | ![product page](https://github.com/Indrakens/sensation-perfume/assets/127971416/95d6dd47-cc59-4aca-9758-dfd1e0336b76)|
| Product Detail Page | ![product detail page](https://github.com/Indrakens/sensation-perfume/assets/127971416/c8205b1e-cc1a-45c1-9226-374d83007083)|
| Shopping Bag Page| ![shopping bag](https://github.com/Indrakens/sensation-perfume/assets/127971416/b5f7a8cf-df0c-40b4-9202-7032e62b49f8)|
| Checkout Page | ![checkout page](https://github.com/Indrakens/sensation-perfume/assets/127971416/f861fa72-9345-492d-9fbd-060365876a44)|
| Product Managemente Page | ![product managemente page ](https://github.com/Indrakens/sensation-perfume/assets/127971416/3f3f4285-79bd-41c3-9441-56e078c4cad5)|
| User Profile Page | ![user profile page](https://github.com/Indrakens/sensation-perfume/assets/127971416/de77bcf7-9437-4f3d-9741-a73a2cf7641c)|
| Blog Post Page | ![blog page](https://github.com/Indrakens/sensation-perfume/assets/127971416/4766df6c-98f8-40ff-bbc2-5faaeb4d4856)|
| Blog Post Detail Page | ![blog detail page](https://github.com/Indrakens/sensation-perfume/assets/127971416/bec3e0fd-3d6d-4834-9faf-cd5856ac79e4)|
### MOBILE
|       |       |
|---------|---------|
| Home Page | ![mobile home page](https://github.com/Indrakens/sensation-perfume/assets/127971416/d702a9ff-da1c-4c15-8310-89f9a0988448)|
| Product Page | ![mobile product page](https://github.com/Indrakens/sensation-perfume/assets/127971416/404b8a5d-19e2-4f8a-bbe1-94b56c847207)|
| Shopping Bag Page | ![mobile shopping bag](https://github.com/Indrakens/sensation-perfume/assets/127971416/96ff3ee7-ff65-458e-ba16-cd97b2d44f97)|
## BUSINESS MODEL 
The business is a B2C e-commerce platform whose goal is to provide products to its customers through an online store. The benefit for a business is easy to scale the business as it grows. Easy to set up a physical location. The business offers perfumes, eau de toilette, giftsets, products for sale- for women and men. Also offers gift wrap for perfumes and eau-de-toilette which is optional. The business marketing strategy is promote the online store trough it's Facebook business page, share the page with friends and family to expanding the business. An online store has a blog section for promoting the product or letting customers know about new product arrivals, which could be productive and sell more products to expand the business. The business goal was to create an online store where shoppers could easily navigate through the website. Provide users with products that meet their expectations, easily add product to shopping bag, and allow them to checkout quickly and easily.
#
## SEO
#### Keywords
Once the business model was decided on as an a perfume store I started working on how to market the site and what keywords to target. I utilised google trends to find more popular search terms. I checked for a number of keywords on google search and I was able to see wich key words are most popular for perfume store. 
#### Sitemap.xml
I generated a sitemap for the site so that once ready engines like google can search it effectively
#### Robots.txt
I generated a robots.txt file so that google could crawl the site. I have blocked off the accounts app as there is no benefit for google to crawl those pages
#
## AGILE
The Agile methodology was used to plan the project. Each user story was linked to an Epic. Issues were used to create Epics and User Stories with a custom template. Once work on the website story was complete, the user story was moved into the "Done" column.
### EPICS
* Shop Management [#5](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=49190188)
* Viewing and Navigation [#7](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=49190730)
* Shopping Bag and Checkout [#8](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=49191015)
* Register an Account [#9](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=49191123)
* Newsletter [#11](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=49192157)
* Login/ Logout [#13](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=51790230)
* Sorting and Searching [#14](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=51791259)
* Shop Facebook Business Page [#32](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=53740551)
* Like / Comment Blog Post [#36](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=53748018)
#
### USER STORIES
The full list of User Stories is available on the project [Sensation Perfume Kanban Board](https://github.com/users/Indrakens/projects/24/views/1). From the Epics 20 User Stories were developed. 
* Shopp Owner
   * As a Store Owner I can add, update, delete products so that I can manage online store [#16](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=51797988)
* User Profile
   * As a User I can easily login so that I can view my profile page [#17](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=51800365)
* Viewing Products
   * As Shopper I can view all lists of products so that I can select some to purchase [#18](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=51801674)
* Navigate Products
   * As a Shopper I can navigate to sales so that I can take advantage of special savings on products I'd like to purchase [#19](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=51803375)      
* Shopping Bag
   * As a Shopper I can view my shopping bag so that I can adjust the shopping bag or go to checkout [#20](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=51805228)  
* Checkout
   * As a Shopper I can go to checkout page so that I can purchase the products I like to order [#21](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=51806372)   
* Product Sorting
   * As a Shopper I can sort list of products so that I can easily identify the best rated, priced and categorically sorted products [#22](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=51810355)  
* Product Searching
   * As a Shopper I can search for the product so that I can find specific product I'd like to purchase [#23](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=51811339)   
* Login/ Logout 
   * As User I can login/ logout so that I can view the website or leave it [#24](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=51812460)  
* Unregistered User
   * As a Unregistered User I can register an account so that I could save my profile [#25](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=51813967)     
* View Number of Likes and Comments
   * As User I can view number of likes and comments so that I can know which are the most liked and commented blog post [#26](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=53733372) 
* Like / Unlike Blog Post
   * As User I can like/unlike blog post so that I can interact with the blog content [#27](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=53734449)
* Comment Blog Post
   * As User I can comment a blog post so that I can interact with the other users in blog detail page [#28](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=53734983)    
* Manage Blog Post
   * As a Shop Admin I can create blog post so that I can publish post or draft post and complete blog post later [#29](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=53737131) 
* Manage Comments
   * As a Shop Admin I can delete comment so that I can filter out inappropriate content [#30](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=53737607)
* Sign Up To Newsletter
   * As a Shopper I can sign up for a newsletter so that I can get access to sales or promotions [#31](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=53739280)
* Facebook Business Page
   * As a Shop Owner I can create Sensation-Perfume business page in Facebook so that I can attract and promote my business to customers through social media [#33](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=53741395)             
* Registering an Account
   * As a User I can register an account so that I can save my order history and have my own profile page [#34](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=53743263)
* View Users
   * As a Shop Admin I can view number of registered users so that I can see how many users are interacting with online shop [#35](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=53744263)    
* View Blog Posts
   * As a User I can can view blog posts so that I can read latest promotions or sales [#37](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=53748971)  
#
## FEATURES
### WEB
#### Navigation Bar 
|         |         |
|-------|---------|
| Logout/ Not Registered User- displays links, logo- redirects user to home page, search bar, free delivery baner, Login/Sign Up link, shopping bag | <img width="946" alt="Screenshot 2024-02-21 235226" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/9b05b3b4-ba23-4d62-bda6-3511bae23852">|
| Login User - displays links, logo- redirects user to home page, search bar, free delivery baner, username Account, shopping bag | <img width="947" alt="Screenshot 2024-02-21 235808" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/ca9e97f9-5a2e-49cf-8fc3-b8514dce907a">|
#### Home Page
|        |       |
|-------|--------|
| Logout/ Not Registered User | <img width="946" alt="Screenshot 2024-02-21 235226" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/26e7c4b2-9f18-489b-a570-4cdd539adcd7">|
| Login User | <img width="947" alt="Screenshot 2024-02-21 235808" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/2e552897-a366-4586-b266-4223c024e09d">|
#### Register Account Page
|      |       |
|------|------|
| Dispays registration form, login link, home link | <img width="952" alt="Screenshot 2024-02-22 012514" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/75e7771e-e817-4568-8988-7f807efee520">|
#### Login Page
|      |       |
|-----|------|
| Displays register link, login form, remeber label, home link, forgot pasword link| <img width="949" alt="Screenshot 2024-02-22 013953" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/12dae2be-6a73-4a87-b504-d8894b5ae7a3">| 
#### Logout Page
|    |      |
|------|-----|
| Displays logout button, home link | <img width="948" alt="Screenshot 2024-02-22 013647" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/7989e0e8-79ee-4c2b-a47e-c2245463e85f">| 
#### Product Page
|      |       |
|-------|-------|
| Displays product image, name, price, category, rating, sort-field, back to top button | <img width="949" alt="Screenshot 2024-02-22 000020" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/c7102e98-2815-48b2-81fa-bfbcb36a2588">|
#### Product Detail Page
|       |       |
|-------|-------|
| Product Detail Page For Him, For Her - Displays product name, price, category, rating, product description, offer gift wrap, quantity, keep shopping button, add to bag button| <img width="945" alt="Screenshot 2024-02-22 003240" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/3492d5b7-ed02-4549-ae28-328270bf0cbb">|
| Product Detail Page Gift Sets - Displays product name, price, category, rating, product description, include, quantity, keep shopping button, add to bag button | <img width="947" alt="Screenshot 2024-02-22 003504" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/d3eabc2b-f693-4944-b575-17e1e76c20f1">|
| Product Detail Page For Him, For Her Sales - Displays product name, price, price was, category, rating, product description, quantity, keep shopping button, add to bag button | <img width="949" alt="Screenshot 2024-02-22 004406" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/da2194dd-54df-4932-9079-fb95c3a60619">|
| Product Detail Page Gift Sets Sales - Displays product name, price, price was, category, rating, product description, include, quantity, keep shopping button, add to bag button| <img width="949" alt="Screenshot 2024-02-22 004555" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/094239ad-505b-4332-87a7-5b2a5ea44a84">| 
#### Blog Post Page
|     |     |
|-----|-----|
| Displays post image, post title, excerpt, created-on, likes, back to top button | <img width="949" alt="Screenshot 2024-02-22 005528" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/23dfaaf1-1e73-4201-97c5-1140e12b58a8">|
#### Blog Post Detail Page
|       |        |
|-------|---------|
|Logout User-displays post image, title, author, content, created-on, number of likes and comments, links to login and register| <img width="946" alt="Screenshot 2024-02-22 010503" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/cec62909-7cab-44e2-9cb0-5fd4190f6a41">|
| Comments Logout User | <img width="950" alt="Screenshot 2024-02-22 010612" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/a0176359-64ec-42fb-8f9c-6f39c96c2fa7">|
|Login User-displays post image, title, author, content, created-on, number of likes and comments| <img width="946" alt="Screenshot 2024-02-22 011230" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/e3002e3c-7746-46dc-9819-ec78400b623b">| 
| Comments Login User - displays comments, comment body | <img width="949" alt="Screenshot 2024-02-22 011440" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/24d534a6-eeae-4264-b4d1-166e4436f28a">|
#### Shopping Bag Page
|      |       |
|--------|-------|
| Displays order info, price, quantity, subtotal, update and remove item, shopping bag total, delivery, total free delivery availability, keep shopping button, checkout button| <img width="951" alt="Screenshot 2024-02-22 014616" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/a8da1f3e-0d30-4a7c-8339-3580297ea1e1">|
#### Checkout Page
|     |      |
|------|-----|
| Displays order form- your details, order owervie| <img width="946" alt="Screenshot 2024-02-22 015014" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/ac8f9a9f-b883-4e0b-8172-694757f5da2f">|
| Displays delivery info, save delivery info tag, add payment, your card charges, adjust bag button, complete order button| <img width="949" alt="Screenshot 2024-02-22 015308" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/3d3a0bf7-8ea1-4518-a006-4ccd99c167d0">|
#### Checkout Success Page
|       |        |
|------|-------|
| Displays order confirmation, checkout the latest sales button, info confirmation email sent to user email| <img width="947" alt="Screenshot 2024-02-22 015803" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/73ce1e93-e462-447a-81b6-7e849009a687">|
### User Profile Page
|       |       |
|------|------|
| Displays user default picture, delivery information, order history, order number link- redirects to past order confirmation page, update profile button, homelink| <img width="949" alt="Screenshot 2024-02-22 020144" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/b8080242-7858-4c69-ad21-604599792599">| 
#### Update User Profile Page
|       |       |
|-------|------| 
| Displays update profile form, select image button, order history, delete order histor, order number link- redirects to past order confirmation page, update button, cancel link| <img width="949" alt="Screenshot 2024-02-22 020746" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/d52feca1-2e6e-4493-99c7-e88f9bd5669c">|
#### Super User - Product Management
|       |      |
|------|------|
| Add Product- displays add product form, select image button, home page link, cancel button, add button| <img width="960" alt="Screenshot 2024-02-22 021014" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/ce5d179e-11b6-4be1-98c5-8ee5d9c931b9">|
| Update and Delete product displayed in product detail page| <img width="947" alt="Screenshot 2024-02-22 021422" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/88f0b0f6-7290-429f-adf4-40efe1f936cd">|
| Update product page - displays update product form, curent image, select image button, cancel button, update product button | <img width="952" alt="Screenshot 2024-02-22 021609" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/1a86c78c-5d05-43e0-87d7-e86da61e99a0">|
#### Footer
|      |      |
|------|------|
| Footer displayed on all pages | <img width="723" alt="Screenshot 2024-02-22 021901" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/ebfeaa0c-65c8-4f97-b11d-125eef85dd1f">|
### MOBILE 
|      |      |
|-------|-----|
| Nav Bar Top- Logout/ Not registered User | <img width="209" alt="Screenshot 2024-02-22 023629" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/c095a64f-8a8f-4844-81ab-497b5eda8cb1">|
| Nav Bar drop down menu | <img width="204" alt="Screenshot 2024-02-22 023840" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/1fed5707-264b-4142-b7fa-418965de03a9">|
| Nav Bar - Login User | <img width="203" alt="Screenshot 2024-02-22 024042" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/00709dea-ef90-4eab-b3b3-f339999528d5">|
| Register Account | <img width="197" alt="Screenshot 2024-02-22 024528" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/faa781c9-d5ea-49f1-80d7-b44ceba6ea69">|
| Login | <img width="207" alt="Screenshot 2024-02-22 024648" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/8838b974-d2ec-4084-829e-e0d8d865537f">|
| Logout | <img width="197" alt="Screenshot 2024-02-22 024326" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/26d7521b-3b2b-46c8-8c25-f5e7da80e51c">|
| Product Page | <img width="207" alt="Screenshot 2024-02-22 024830" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/8973fdfa-1025-41ae-994c-cf63fa297d81">|
| Product Detail Page  | <img width="207" alt="Screenshot 2024-02-22 025151" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/3ca90bd9-b8dc-4456-846b-44d43b6bad30">|
| Continues Product Detail Page | <img width="212" alt="Screenshot 2024-02-22 025442" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/3e8f52fa-cc4f-4f44-9a63-e6fb540d0ee5">|
| Shopping Bag | <img width="208" alt="Screenshot 2024-02-22 025646" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/2d7c54df-4ab9-496e-85fb-c4d096fab342">|
| Checkout Page | <img width="210" alt="Screenshot 2024-02-22 025808" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/5580fbaa-3906-4373-922f-edd405a6a6fd">|
| Checkout Success Page | <img width="205" alt="Screenshot 2024-02-22 030042" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/4405e939-dadb-441c-a8ac-81e9ae7055f8">|
| Blog Page | <img width="215" alt="Screenshot 2024-02-22 030233" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/7b7cf25d-2eb9-4824-ad23-e09312c8446b">|
| Blog Post Detail Page | <img width="219" alt="Screenshot 2024-02-22 030438" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/18a4597f-b1bc-4b55-9ef9-fc9d54426344">|
| Blog Blog Post Detail Page comments - Logout/ not Registered User | <img width="212" alt="Screenshot 2024-02-22 030639" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/e152b8a4-daef-4e14-9b93-791e42cb3422">|
| Blog Blog Post Detail Page comments - Login User | <img width="219" alt="Screenshot 2024-02-22 031118" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/6dd22e11-825c-4ed2-9881-d42293bd01d4">| 
| Footer | <img width="216" alt="Screenshot 2024-02-22 031406" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/b5299b5c-644c-432c-8bae-830cd7d5667f">|
#
## FACEBOOK
|        |          |
|--------|--------|
| Header | <img width="955" alt="Screenshot 2024-02-20 194046" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/16cc5277-7f55-4865-9b8a-615e0d222531">|
| Intro  | <img width="961" alt="Screenshot 2024-02-19 190950" src="https://github.com/Indrakens/sensation-perfume/assets/127971416/413348c9-4931-4e9f-9089-3d06d3603f56">|
## TESTING
Full testing can be seen in [TESTING.md](https://github.com/Indrakens/sensation-perfume/blob/main/TESTING.md) file.
## TEHNOLOGY USED
#### [HTML](https://en.wikipedia.org/wiki/HTML) - Used to build the front-end website
#### [CSS](https://en.wikipedia.org/wiki/CSS) - Used to style the HTML
#### [JavaScript](https://www.javascript.com/) - Used to add card payment, country field, sorting products, back to top click function, update the item quantity, and remove the item from the shopping bag
#### [Python](https://www.python.org/) - Used as the back-end programming language
#### [Django](https://www.djangoproject.com/) - Used as the Python framework for the website. 
#### [Bootstrap](https://getbootstrap.com/) - Used as the front-end framework for responsiveness and pre-built components
#### [Git](https://git-scm.com/) - Used for version control
#### [GitHub](https://github.com/) - Used for online code storage
#### [GitPod](https://www.gitpod.io/) - Used as a cloud-based IDE for development
#### [ElephantSQL](https://customer.elephantsql.com/login) - Used as the Postgres database 
#### [Heroku](https://id.heroku.com/) - Used for cloud based platform for deployment  
#### [Gunicorn](https://gunicorn.org/) - Used as a website server provider
#### [Psycopg2](https://pypi.org/project/psycopg2/) - Used as a postgres database adapter
#### [AWS S3 and IAM](https://aws.amazon.com/) - Used to host static and media files for this project and IAM for the permissions based roles for accessing the S3 buckets
#### [Stripe](https://stripe.com/ie) - Used handle secure payments 
#### [XML-Sitemaps](https://www.xml-sitemaps.com/) - Used to generate Sensation-Perfume sitemap
#### [Privacy Policy Generator](https://www.privacypolicygenerator.info/) - Used to generate Sensation-Perfume privacy policy
#### [Mailchimp](https://mailchimp.com/?currency=EUR) - Used to set up Sensation-Perfume newsletter email marketing 
## FEATURE TO IMPLEMENT
* Users can edit or delete their own commented comments
* Registered users can delete their account from web. At the moment only admin can delete user in admin panel
## BUG
* I wasn't able to set up a user profile image to nav link my profile instead of an icon. It was only visible when you were on the profile page. Also, the user profile image didn't appear in the comments when the user commented. 
## DEPLOYMENT
* Sign-up / Log-in to [Heroku](https://www.heroku.com/home)
* From the main Heroku Dashboard page select 'New' and then 'Create New App'
* Give the project a name (app name must be unique) and select a suitable region, then select create app
* Heroku will create the app and bring you to the deploy tab
* From the submenu at the top, navigate to the resources tab
* Add the database to the app, in the add-ons section search for 'Heroku Postgres', select the package that appears and add 'Heroku Postgres' as the database
* Click on the setting tab
* In the Heroku settings tab of your project update the config vars to the following:
|  Key      |    Value       |
|---------|---------:|
| AWS_ACCESS_KEY_ID     | From AWS in CSV Download |
| AWS_SECRET_ACCESS_KEY | From AWS in CSV Download |
| DATABASE_URL          | From ElephantSQL dashboard |
| EMAIL_HOST_PASSWORD   | App Password from Email Client |
| EMAIL_HOST_USER       | Email address |
| SECRET_KEY            | Randomly Generated Django Key |
| STRIPE_PUBLIC_KEY     | Publishable key from Stripe Dashboard |
| STRIPE_SECRET_KEY     | Secret key from Stripe Dashboard |
| STRIPE_WH_SECRET      | Signing secret from Stripe Webhooks Endpoint |
| USE_AWS               | True |
* If you deploy at the beginning of the project then add the key value of: DISABLE_COLLCETSTATIC and set it to 1. When you have staticfiles to push then remove this variable
* Once the project is completed and you are no longer working on it set DEBUG = False in settings.py
* Log in to Heroku and select the deploy tab on your Heroku App and connect your GitHub account
* Search for your repository and connect it
* Once you have selected the correct repository, scroll down and click "Deploy Branch"
* Watch the log as it deploys your project and ensure there are no errors
* If everything is correct it should deploy successfully
* Click on open app at the top of the page to view your deployed app
## FORKING AND CLONING
### Forking The Repository 
By forking the GitHub Repository you can make a copy of the original repository to view or change without it effecting the original repository
* Logging into GitHub or create an account
* Locate the repository [https://github.com/Indrakens/sensation-perfume](https://github.com/Indrakens/sensation-perfume)
* At the top of the repository, on the right side of the page, select "Fork" from the buttons available
* A copy of the repository should now be created in your own repository
### Create A Clone Of Repository
Creating a clone enables you to make a copy of the repository at that point in time - this lets you run a copy of the project locally
* Navigate to [https://github.com/Indrakens/sensation-perfume](https://github.com/Indrakens/sensation-perfume)
* Click on the arrow on the green code button at the top of the list of files
* Select the clone by https option and copy the URL it provides to the clipboard
* Navigate to your code editor of choice and within the terminal change the directory to the location you want to clone the repository to
* Type 'git clone' and paste the https link you copied from github
* Press enter and git will clone the repository to your local machine 
## CONTENT AND RESOURCES
#### Django Documentation
* Read through the django documentation multiple times
* Used extensively during development of this project
#### W3 Schools
* Used for reference throughout for simple css examples
#### Code Institute
* The Code Institute reference material was used as a general reference for things that I had previously done during the course
* Course content for portfolio project 4 helped able to complete this project
## ACKNOWLEDGMENT
* Graeme Taylor - my mentor who provided me with great feedback and guidance at the inception of this projec
* Alan Bushell - our teacher, always a great mentor during stand-up. And who helped insure me to get true this project
* To all the tutors in Code Institute were always on hand to answer any queries or questions if things got too difficult