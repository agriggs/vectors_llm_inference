# Embeddings and Vector Databases With ChromaDB

Supporting code for the Real Python tutorial [Embeddings and Vector Databases With ChromaDB](https://realpython.com/chromadb-vector-database/). 

## API Keys
Get OpenAI and Google Gemini API keys and set environment variables
```
OPENAI_API_KEY
GOOGLE_API_KEY
ANTHROPIC_API_KEY
```

Restart VS Code or other IDE so the environment variables are loaded

## Python Environment

Create the virtual environment
```
python -m venv .venv
```

Activate the virtual environment
```
.\.venv\Scripts\activate
```

Install the Python packages to the virtual environment
```
pip install -r .\requirements.txt
```

If running behind a TLS intercept (on corporate network), may need to set these environment variables for Python libs: requests, httpx
```
REQUESTS_CA_BUNDLE
SSL_CERT_FILE
```

## Create the RAG vectors
```
python create_car_review_collection.py
```

## Run GenAI Inference

OpenAI 
```
python llm_car_review_context_unified.py openai
```

Gemini 
```
python llm_car_review_context_unified.py gemini
```

Claude
```
python llm_car_review_context_unified.py claude
```

## Example Outputs

### Elasticsearch Semantic Output

<b>Good reviews</b>

Great value, awesome reliability, I normally dont do reviews, but thought this was worth writing. I own 3 pickups and am not brand dedicated because there are so many nice trucks. I own 3 different trucks. I am drawn to looks first then power and interior. I have notice reading reviews that most want to beat the trucks up, there are no perfect trucks. The Nissan drew me in because it was different and I dont recall any recalls. I owned a Xterra and it was bulletproof and am hoping for the same on my Titan. After looking at all brands and I liked them all, I really like the warranty on my Titan and I got more equipment for the money than the competitors. My first and second tank of fuel at 70 mpg I got 17.5, I was very pleased and when it get broke in I hope for 20. I find it to be very quiet and so were all the others on top of the line. I guess I could beat the truck up with small complaints but sure makes spending my money on it hard to swallow. If the truck last me for 10 years I will be very pleased. I know the ride will get much better as it has in all my cars and trucks in time. I hope you enjoy your new purchase as much as I am enjoying mine., Very  pleased! Great deal! So far so good!, Excellent quality, technology, comfort and value. Way impressed with this vehicle., Things I love: styling, performance, large info center, smooth acceleration, no gas stations, low maintenance costs, incredible sound system, frunk and sub-trunk, rear cargo space, HOV lane, federal tax credit, summons feature, replacement parts seem nicely priced, my first Service Center experience was excellent, my first body shop experience was very good, many people think you are "cool" and environmentally friendly (and you are).          Things I wish were better: fit and finish of body parts (not up to premium car standard), auto pilot still not a wow...needs more development, blind spot monitor is below expectations for such an advance vehicle, difficulty getting in and out of front seat...if you are tall, the front seat goes behind the "B" pillar too far thus the entering and exiting is more difficult. Final Verdict. I love the car. I doubt I would ever buy an ICE car again., Good overall but a lot of others out there., Excellent choice, so far, so good.  I got the S-Line, Premium Plus package and am very happy with it.  Quality it top notch inside and out.  No issues at all, though I've only had it for a month and about 1500 miles., After all the facts and findings over all review is outstanding., Excellent features and performance!  

<b>Worst reviews:</b> 

 I have been to the dealership four times and I still have unresolved electrical issues, from the Bluetooth, backup camera, truck wont open, black screen every other trip turning off, clock wont work, seatbelts NOT WORKING !!!!!!!! which really pisses me off as I have a child in the car. So many issues in a short period of time it has become the worst vehicle I have owned unfortunately and to the point where I will drop the car off back at the dealership and purchase something else. I don't have the time to deal with a vehicle of 53k value as if it were pieced together from spare parts from a junkyard. I always read reviews before buying vehicles and I have stuck with Nissan & Infiniti for the past ten years for their workhorse engines as two of my Nissans went to 289k & 377k miles but after this SUV I am jumping ship as soon as possible.

### OpenAI

<b>OpenAI generated summary with gpt-3.5-turbo of good reviews:</b>

Based on the detailed positive reviews provided, the key to great customer satisfaction seems to be a combination of several factors:

1. **Value for Money**: Customers appreciate getting a good deal and feeling like they are getting more equipment for their money compared to competitors.

2. **Reliability**: Customers value reliability and durability in a product. Knowing that the vehicle is well-built and has a good track record can greatly enhance satisfaction.

3. **Performance**: Customers are drawn to vehicles that offer good performance, whether it's in terms of power, acceleration, or fuel efficiency.

4. **Quality**: High-quality materials and technology contribute to a positive experience for customers. Features like a great sound system, comfortable interior, and advanced technology can enhance satisfaction.

5. **Customer Service**: Positive experiences with service centers and body shops can also contribute to overall satisfaction. Good customer service can make the ownership experience more pleasant.

6. **Warranty**: A good warranty can provide peace of mind for customers, knowing that they are covered in case of any issues.

7. **Enjoyment**: Ultimately, customers want to enjoy their purchase and feel good about their decision. If the product meets or exceeds their expectations and brings them joy, they are likely to be highly satisfied.

By focusing on these aspects - value, reliability, performance, quality, customer service, warranty, and overall enjoyment - businesses can enhance customer satisfaction and loyalty.

<b>OpenAI generated summary with gpt-3.5-turbo of the single worst review:</b>

The review that has the worst implications about your dealership is the first one, where the customer expresses frustration with unresolved electrical issues in their vehicle. The customer mentions multiple issues such as problems with Bluetooth, backup camera, trunk not opening, black screen, clock not working, and seatbelts not working, which is a serious safety concern, especially since they have a child in the car. The customer also expresses disappointment in the quality of the vehicle, comparing it unfavorably to their previous experiences with Nissan and Infiniti vehicles.     

This review reflects poorly on the dealership because it indicates that the dealership has not been able to effectively address and resolve the customer's concerns despite multiple visits. The customer's dissatisfaction with the vehicle and the dealership's inability to fix the issues in a timely manner may lead to a loss of trust in the dealership's service and the quality of the vehicles they sell. It also suggests a lack of attentiton detail and customer care, which can have long-lasting negative implications for the dealership's reputation and customer loyalty.

### Gemini

<b>Gemini generated summary with gemini-2.5-flash of good reviews:</b>

As a customer success employee, analyzing these detailed positive reviews reveals that the key to great customer satisfaction isn't just one thing, but a powerful combination of factors that address both practical needs and emotional desires, often exceeding initial expectations.

Here's a breakdown of the key elements:

1.  **Exceptional Value & Long-Term Peace of Mind:**
    *   **What customers say:** "Great value," "Great deal," "more equipment for the money," "100K powertrain warranty and lifetime battery warranty I am covered," "no recalls," "low maintenance costs," "federal tax credit," "replacement parts seem nicely priced."
    *   **Our takeaway:** Customers are looking for more than just a good price; they want to feel they're getting *more* for their money (features, equipment) and that their investment is protected long-term. Robust warranties, a reputation for reliability, and clear communication about potential savings (fuel, maintenance, tax credits) are huge drivers of satisfaction and reduce buyer's remorse.

2.  **Performance & Efficiency that Exceeds Expectations:**
    *   **What customers say:** "blown away," "most economical, practical, comfortable commuter vehicle," "averaging close to 80 MPGs," "very pleased" with 17.5 MPG (when expecting less), "ghostly silent," "smooth acceleration," "no gas stations."
    *   **Our takeaway:** When a vehicle performs better than anticipated, especially in areas like fuel economy, quietness, or power, it creates a "wow" factor. Highlighting specific, measurable benefits that solve a customer's pain point (like frequent gas station trips for the commuter) turns a good car into a beloved one.

3.  **Comfort, Quality, and Thoughtful Design:**
    *   **What customers say:** "awesome reliability," "drawn to looks first then power and interior," "very quiet," "perfect driving position, comfortable seating and good ergonomics," "impressed with ride and build quality," "Excellent quality, technology, comfort," "Quality it top notch inside and out," "styling," "large info center," "incredible sound system."
    *   **Our takeaway:** While subjective, consistent praise for interior comfort, quietness, ride quality, and overall build quality is crucial. Customers appreciate a well-designed, high-quality interior and exterior that feels good to drive and look at. Even small details like ergonomics or a great sound system contribute significantly.

4.  **A Transformative & Problem-Solving Experience:**
    *   **What customers say:** "I was tired of the constant trips to gas stations and the expense. After just a month with this car, I am blown away," "I love the car. I doubt I would ever buy an ICE car again," "many people think you are 'cool' and environmentally friendly (and you are)."
    *   **Our takeaway:** The best satisfaction comes when a vehicle fundamentally changes a customer's daily life for the better or aligns with their values. Whether it's eliminating gas station stops, providing a sense of environmental responsibility, or simply making a long commute enjoyable, connecting the vehicle to a deeper, positive lifestyle change creates immense loyalty.

5.  **Exceptional Post-Sale Service & Support (Our Direct Impact!):**
    *   **What customers say:** "my first Service Center experience was excellent, my first body shop experience was very good."
    *   **Our takeaway:** This is where *we* as a dealership shine. Even with a fantastic product, a poor service experience can sour a customer's overall satisfaction. Proactive, efficient, and friendly service (both routine maintenance and unexpected repairs) reinforces the initial positive purchase decision and builds trust, ensuring repeat business and positive word-of-mouth.

In summary, the key to great customer satisfaction is to deliver a vehicle that offers **outstanding value and long-term peace of mind**, **exceeds expectations in performance and efficiency**, provides **superior comfort, quality, and thoughtful design**, and ultimately offers a **transformative, problem-solving experience**. Crucially, all of this must be backed by **exceptional post-sale service and support** from our dealership. When we consistently hit these marks, customers don't just buy a car; they become advocates.

<b>Gemini generated summary with gemini-2.5-flash of the single worst review:</b> 

The review with the worst implications about our dealership is the **first one, regarding the Nissan/Infiniti with unresolved electrical issues and non-working seatbelts.**

Here's why:

1.  **Critical Safety Failure:** The most damning statement is "seatbelts NOT WORKING !!!!!!!! which really pisses me off as I have a child in the car." This is an absolute, non-negotiable safety defect. A dealership's primary responsibility, especially in its service department, is to ensure the vehicles it sells and services are safe. Failing to fix non-functional seatbelts directly endangers lives, particularly a child's.
2.  **Repeated Service Failure:** The customer states, "I have been to the dealership four times and I still have unresolved electrical issues." This indicates a systemic failure in our service department. Not only did we fail to fix critical issues, but we failed *repeatedly* over multiple visits. This suggests incompetence, lack of thoroughness, or an inability to diagnose and repair complex problems.
3.  **Complete Loss of Trust and Loyalty:** This customer was a loyal Nissan & Infiniti owner for ten years, with vehicles lasting hundreds of thousands of miles. This review signifies a complete and utter breakdown of trust, leading them to "jump ship as soon as possible" and even "drop the car off back at the dealership and purchase something else." Losing a long-term, loyal customer due to such severe and unresolved issues is a significant blow.
4.  **Damaging Public Perception:** This review paints a picture of a dealership that sells unreliable vehicles and, more critically, cannot fix dangerous safety defects. For potential customers reading this, the message is clear: this dealership cannot be trusted with their safety or their money. The comparison to a vehicle "pieced together from spare parts from a junkyard" for a $53k value is incredibly damaging to our reputation for quality and value.

While other reviews mention significant issues (like the Honda review's "nasty view of their customers" and safety concerns on a new truck, or the GMC review's major mechanical problems and parts delays), the Nissan/Infiniti review stands out due to the direct, repeated failure to resolve a life-threatening safety issue, leading to the complete alienation of a previously loyal customer. This directly attacks the core competence and trustworthiness of our service department and, by extension, the entire dealership.

### Claude

<b>Claude generated summary with claude-sonnet-4-5 of good reviews:</b> 
Based on the detailed positive reviews provided, the keys to great customer satisfaction are:

#### 1. **Value for Money**
Customers emphasize getting "more equipment for the money than competitors" and appreciate "great deals." The perception of receiving excellent features at a competitive price point is crucial.

#### 2. **Reliability and Quality**
Multiple reviews mention "awesome reliability," "bulletproof" performance, and "excellent quality." Customers want vehicles they can trust for the long term (10+ years).

#### 3. **Strong Warranty and Low Maintenance**
A generous warranty package and "low maintenance costs" provide peace of mind and reduce long-term ownership concerns.

#### 4. **Performance and Technology**
Customers value:
- "Smooth acceleration" and performance
- Advanced technology features (large info centers, autopilot, summons features)
- Modern amenities (sound systems, cargo space)

#### 5. **Unique Features and Differentiation**
Buyers appreciate vehicles that are "different" and stand out, whether through styling, environmental benefits (HOV lanes, no gas stations), or innovative features.

#### 6. **Positive Ownership Experience**
- Good service center experiences
- Fair replacement part pricing
- Meeting or exceeding expectations (fuel economy, comfort)

**Bottom Line**: Great customer satisfaction comes from delivering reliable, feature-rich vehicles at competitive prices, backed by strong warranties and excellent service—essentially exceeding value expectations while minimizing ownership hassles.

<b>Claude generated summary with claude-sonnet-4-5 of the single worst review:</b>

Based on these reviews, **the second review (about the GMC vehicle with transmission issues)** has the worst implications for the dealership, despite the reviewer noting the dealer has been "very good to work with."

Here's why this is most damaging:

#### Critical Safety and Operations Issues:

1. **Repeated, Extended Downtime**: The vehicle has been in the shop for 14 days across 3 occasions and is STILL there. This suggests:
   - Inability to diagnose problems correctly the first time
   - Poor parts inventory management
   - Inefficient service operations

2. **Parts Availability Crisis**: The dealership didn't have basic parts on hand for multiple repairs:
   - Transmission leak parts
   - Spindle nut (which was broken by the mechanic)
   - Rear shock and spring bushing components

   This reveals systematic inventory problems that extend repair times unnecessarily.

3. **Mechanic Error**: Breaking the spindle nut during reassembly shows potential technician competency issues or rushing through repairs.

4. **Factory Defect Not Caught**: The rear wheel alignment issue that wore tires to the cord should have been caught during pre-delivery inspection (PDI). This is a fundamental dealership failure. 

5. **Potential Lemon**: The customer is explicitly considering this a lemon, which could lead to legal action involving the dealership.

#### Why This is Worse Than the Others:

- **Review 1 (Nissan/Infiniti)**: Focuses on vehicle quality issues, not dealership service failures
- **Reviews 3, 4, 5**: Focus on vehicle design/comfort complaints, not dealership operations

The GMC review reveals operational incompetence that reflects directly on YOUR dealership's service department, parts management, and quality control processes.