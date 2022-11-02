var company_email = document.getElementById('company_email')

//check email 
function validateEmail() {
    var email = company_email.value;
    var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
    if (!emailReg.test(email)) {
        company_email.setCustomValidity('Please enter a valid email address');
    } else {
        company_email.setCustomValidity('');
    }
}