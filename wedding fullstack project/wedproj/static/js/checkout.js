
    var payWithRazorpay = document.querySelector('.payWithRazorpay')
    document.addEventListener("DOMContentLoaded", function (){
    
        payWithRazorpay.addEventListener('click',function(e){
            e.preventDefault();

            var gname = document.querySelector('input[name="gname"]').value;
            var bname = document.querySelector('input[name="gname"]').value;
            var email = document.querySelector('input[name="email"]').value;
            var occ_date = document.querySelector('input[name="occ_date"]').value;

            if(gname == "" || bname == "" || email =="" || occ_date == "")
            {
                alert("All feilds are mandatory");
                return false;
            }
            else
            {

                fetch('/proceed_to_pay', {
                    method: 'GET',
                    headers:{
                        'Accept': 'application/json',
                        'X-CSRFToken': '{{ csrf_token }}'
                    },
                    

                }).then(response => response.json())
                //.then(response => console.log((response)))*/
                
                    
                
                

                    var options = {
                    "key": "rzp_test_bVl6pURdksjoq6", // Enter the Key ID generated from the Dashboard
                    "amount": "{{total_price}}", // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                    "currency": "INR",
                    "name": "The Perfect Knot", //your business name
                    "description": "Thank You for choosing us!",
                    "image": "https://example.com/your_logo",
                    "order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                    "handler": function (responseb){
                        alert(responseb.razorpay_payment_id);
                        data={
                            "gname":gname,
                            "bname":bname,
                            "email":email,
                            "occ_date":occ_date
                        }
                    },
                    "prefill":{
                        "name":gname+" "+bname,
                        "email":email
                    },
                    "theme": {
                        "color": "#3399cc"
                    }
                };
                var rzp1 = new Razorpay(options);
                //document.getElementsByClassName('payWithRazorpay').onclick = function(pay){
                    rzp1.open();
                   // pay.preventDefault();
                //}
        
                
           }
            
        });
    });
    

