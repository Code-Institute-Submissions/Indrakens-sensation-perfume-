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
* [UX](https://github.com/Indrakens/sensation-perfume/tree/main?tab=readme-ov-file#ux)
* [UX DESIGN](https://github.com/Indrakens/sensation-perfume/tree/main?tab=readme-ov-file#ux-design) 
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
   * [WEB](https://github.com/Indrakens/sensation-perfume/tree/main?tab=readme-ov-file#web-1)
   * [MOBILE](https://github.com/Indrakens/sensation-perfume/tree/main?tab=readme-ov-file#mobile-1)
* [FACEBOOK](https://github.com/Indrakens/sensation-perfume/tree/main?tab=readme-ov-file#facebook)    
* [TESTING](https://github.com/Indrakens/sensation-perfume?tab=readme-ov-file#testing)
* [TEHNOLOGY USED](https://github.com/Indrakens/sensation-perfume?tab=readme-ov-file#tehnology-used)
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
| Conceptual ERD | ![erd](https://github.com/Indrakens/sensation-perfume/assets/127971416/9e14bfd6-bdfb-4971-9b36-bf895d17e546)|
#
## WIREFRAMES
### WEB
|        |          |
|----------|----------|
| Home Page | ![home no logged in user](https://github.com/Indrakens/sensation-perfume/assets/127971416/8ed9232b-9316-4a22-b790-edb263760b0f)|
| Product Page | ![product page](https://github.com/Indrakens/sensation-perfume/assets/127971416/72c4171a-8f91-49eb-b97e-9438c72fdf1d)|
| Product Detail Page With Review - Login User | ![user product detail page (1)](https://github.com/Indrakens/sensation-perfume/assets/127971416/124cc486-61d1-44f0-8ad7-3345bd7ac73e)|
| Product Detail Page Without Review - Login User | ![login user no raiting and reviews detail page (1)](https://github.com/Indrakens/sensation-perfume/assets/127971416/a360eb5a-aa22-43da-ad61-d5a0d1fc56b6)|
| Super User Product Detail Page with reviews | ![super user p-detail page with revies and included giftwrap (1)](https://github.com/Indrakens/sensation-perfume/assets/127971416/1335e4e0-fb86-4423-8b7a-9cc72293b6bb)|
| Shopping Bag Page| ![shopping bag (2)](https://github.com/Indrakens/sensation-perfume/assets/127971416/6d226467-a255-4aa2-a687-5cfed854c73e)|
| Checkout Page | ![checkout (1)](https://github.com/Indrakens/sensation-perfume/assets/127971416/ec1226d3-c1e2-4ff5-bba2-370b37fb3faa)|
| Product Managemente - Add Product Page | ![management add product (1)](https://github.com/Indrakens/sensation-perfume/assets/127971416/d8edf98b-6650-4a6f-bf3a-ec42710f06ca)|
|  Product Managemente - Update Product Page | ![management update product (1)](https://github.com/Indrakens/sensation-perfume/assets/127971416/bb0f463c-d6c5-4fb2-b3d2-8f3a1d75f69e)|
| Contact Us Page | ![contact us form (1)](https://github.com/Indrakens/sensation-perfume/assets/127971416/fb56430e-2023-4f36-bc4b-85e2406414ff)|

### MOBILE
|       |       |
|---------|---------|
| Home Page | ![mobile home (1)](https://github.com/Indrakens/sensation-perfume/assets/127971416/ed8ac83f-0580-436f-bb25-8f75a94b526c)|
| Product Page | ![mobail all products (1)](https://github.com/Indrakens/sensation-perfume/assets/127971416/0e5f2810-267a-4aaa-8e09-9354c9ff8a50)|
| Product detail Page without reviews - Not Logged in User | ![no loedin user detail page no rating (1)](https://github.com/Indrakens/sensation-perfume/assets/127971416/ca97a864-5531-4940-bfb2-a1ed8eac7319)|
| Product detail Page with reviews - Not Logged in User | ![no loedin user detail page (1)](https://github.com/Indrakens/sensation-perfume/assets/127971416/afb22ae2-9d2c-4a90-917c-a4803f714e9f)|
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
* Product Review [#42](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=59130849)
* Contact Form [#43](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=59132777)
#
### USER STORIES
The full list of User Stories is available on the project [Sensation Perfume Kanban Board](https://github.com/users/Indrakens/projects/24/views/1). From the Epics 22 User Stories were developed. 
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
* Product Review
   * As a User I can can leave a review to the products so that I can I can let know product like/dislike [#44](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=59133249)
* Contact Us
   * As a User I can can contact the business owner so that I can notify about my query [#45](https://github.com/users/Indrakens/projects/24/views/1?pane=issue&itemId=59134472)  
#
## FEATURES
### WEB
#### Navigation Bar 
|         |         |
|-------|---------|
| Logout/ Not Registered User- displays links, logo- redirects user to home page, search bar, free delivery baner, Login/Sign Up link, shopping bag | ![Screenshot 2024-04-09 103858](https://github.com/Indrakens/sensation-perfume/assets/127971416/b05539d1-395f-4b45-be75-29dca936a634)|
| Login User - displays links, logo- redirects user to home page, search bar, free delivery baner, username Account, shopping bag | ![Screenshot 2024-04-09 104216](https://github.com/Indrakens/sensation-perfume/assets/127971416/119ba3f2-6657-487b-8e16-98fa4d9e431b)|
#### Home Page
|        |       |
|-------|--------|
| Logout/ Not Registered User | ![Screenshot 2024-04-09 104520](https://github.com/Indrakens/sensation-perfume/assets/127971416/63e5ac33-8a21-4ad8-b27d-96781a0e013c)|
| Login User | ![Screenshot 2024-04-09 104355](https://github.com/Indrakens/sensation-perfume/assets/127971416/8d349f8e-cd8f-49b2-a3f2-1ab644e1b449)|
#### Register Account Page
|      |       |
|------|------|
| Dispays registration form, login link, return to home link | ![Screenshot 2024-04-09 104707](https://github.com/Indrakens/sensation-perfume/assets/127971416/f333ccf4-97af-4a2e-8ed3-ea82a921cb65)|
#### Login Page
|      |       |
|-----|------|
| Displays register link, login form, remeber label, return to home link, forgot pasword link| ![Screenshot 2024-04-09 104857](https://github.com/Indrakens/sensation-perfume/assets/127971416/6bf74488-a2ae-4a0f-aa05-3703eb97b5d6)| 
#### Logout Page
|    |      |
|------|-----|
| Displays logout button, return to home link | ![Screenshot 2024-04-09 105129](https://github.com/Indrakens/sensation-perfume/assets/127971416/e228efad-fca2-47af-a397-e1e288d8bbed)| 
#### Product Page
|      |       |
|-------|-------|
| Displays product image, name, price, category, brand, gender, rating, sort-field, back to top button | ![Screenshot 2024-04-09 105344](https://github.com/Indrakens/sensation-perfume/assets/127971416/efa72f82-53de-48dd-822f-9f0ae41956cf)|
#### Product Detail Page
|       |       |
|-------|-------|
| Product Detail Page - Displays product name, price, price was, category, brand, gender,rating, review-comment, review form for login users, product description, delivery banner, offer gift wrap, include, quantity, add to bag button| ![Screenshot 2024-04-09 105749](https://github.com/Indrakens/sensation-perfume/assets/127971416/c7493b33-5466-4e18-9f66-5c98341eb5ab)|
| Product Detail Page Review  - Displays review form - login users only, added review with rating, date, commented by, comment | ![Screenshot 2024-04-09 110319](https://github.com/Indrakens/sensation-perfume/assets/127971416/14579329-89a5-4780-8d5c-1525cd4a7b7a)|
#### Shopping Bag Page
|      |       |
|--------|-------|
| Displays order info, price, quantity, subtotal, update and remove item, shopping bag total, delivery, total free delivery availability, checkout button, continue shopping link| ![Screenshot 2024-04-09 110618](https://github.com/Indrakens/sensation-perfume/assets/127971416/50a923bf-f26b-4f5c-bb13-ecc9f1e724e6)|
#### Checkout Page
|     |      |
|------|-----|
| Displays order form- your details, order owervie| ![Screenshot 2024-04-09 110912](https://github.com/Indrakens/sensation-perfume/assets/127971416/5bb5fed2-2c67-40a0-8917-de405920846a)|
| Displays delivery info, save delivery info tag, add payment, your card charges, complete order button, return to shopping bag link| ![Screenshot 2024-04-09 111015](https://github.com/Indrakens/sensation-perfume/assets/127971416/df183c77-a19b-45d3-917c-199ccfdc2889)|
#### Checkout Success Page
|       |        |
|------|-------|
| Displays order confirmation, checkout the latest sales button, info confirmation email sent to user email| ![Screenshot 2024-04-09 111142](https://github.com/Indrakens/sensation-perfume/assets/127971416/8adf5080-6ced-4776-b6aa-3cce08ad81cb)|
### User Profile Page
|       |       |
|------|------|
| Displays user default picture, delivery information, order history, order number link- redirects to past order confirmation page, update profile button, return to home link| ![Screenshot 2024-04-09 111310](https://github.com/Indrakens/sensation-perfume/assets/127971416/cc27f87e-20be-44f8-a3c1-c861ce21c8e4)| 
#### Update User Profile Page
|       |       |
|-------|------| 
| Displays update profile form, select image button, order history, delete order histor, order number link- redirects to past order confirmation page, update button, return to username profile page link| ![Screenshot 2024-04-09 111527](https://github.com/Indrakens/sensation-perfume/assets/127971416/21a5afbd-ae87-4ff6-b8ff-7ae8bf45c36d)|
#### Super User - Product Management
|       |      |
|------|------|
| Add Product- displays add product form, select image button, home page link, add button, return to home page link| ![Screenshot 2024-04-09 111821](https://github.com/Indrakens/sensation-perfume/assets/127971416/d7763e00-d20a-4e41-ad6f-7f30f4750a30)|
| Update and Delete product displayed in product detail page| ![Screenshot 2024-04-09 111943](https://github.com/Indrakens/sensation-perfume/assets/127971416/0728e850-e139-4b00-a762-c018435345ae)|
| Update product page - displays update product form, curent image, select image button, update product button, return to product name page link | ![Screenshot 2024-04-09 112056](https://github.com/Indrakens/sensation-perfume/assets/127971416/bbf6ee2b-7410-4a5b-8807-7d6bd114736b)|
#### Contact Us
|      |       |
|-----|-------|
| Contact Us  displays contact form, submit button, return to home link | ![Screenshot 2024-04-09 112656](https://github.com/Indrakens/sensation-perfume/assets/127971416/89730e56-14ce-4b90-a7c6-528e1758f59c)|
#### Footer
|      |      |
|------|------|
| Footer displayed on all pages | ![Screenshot 2024-04-09 112252](https://github.com/Indrakens/sensation-perfume/assets/127971416/d83a2b19-31ce-493b-bfc2-d02e06e7678e)| 
### MOBILE 
|      |      |
|-------|-----|
| Nav Bar Top- Logout/ Not registered User | ![Screenshot 2024-04-09 112449](https://github.com/Indrakens/sensation-perfume/assets/127971416/c71e5827-497b-42a7-8c33-bf0d3c831735)|
| Product Page | ![Screenshot 2024-04-09 112950](https://github.com/Indrakens/sensation-perfume/assets/127971416/4ebadf2a-8947-41a6-bfb4-e1879d880b8b)|
| Product Detail Page  | ![Screenshot 2024-04-09 113142](https://github.com/Indrakens/sensation-perfume/assets/127971416/29b0ccf6-49a1-4f95-9723-06b41b3843ce)|
| Continues Product Detail Page reviews form - login users only, review |  ![Screenshot 2024-04-09 113329](https://github.com/Indrakens/sensation-perfume/assets/127971416/f41637d7-6e27-4d35-9808-a16f4f2ea3e8)|
| Continues Product Detail Page description, delivery banner, offer gift wrap, quantity, add to bag button| ![Screenshot 2024-04-09 113640](https://github.com/Indrakens/sensation-perfume/assets/127971416/29db4bec-f058-43bb-9a8e-b82525b54bad)|
| Footer | ![Screenshot 2024-04-09 113828](https://github.com/Indrakens/sensation-perfume/assets/127971416/b1b4be69-a324-44a4-80f2-d5e0ae8f2a42)|
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