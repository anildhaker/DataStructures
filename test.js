var car = {
  registrationNumber: "T12345",
  brand: "ABC",

  displayDetails:  function() {
    console.log(this.registrationNumber + " " + this.brand);
  }
}

var myCarDetails = car.displayDetails();
myCarDetails;