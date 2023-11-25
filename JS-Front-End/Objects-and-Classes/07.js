function addressBook(array) {
    let addressBookObject = {};

    for (let element of array) {
        let [key, value] = element.split(":");
        addressBookObject[key] = value;
    }

    Object.keys(addressBookObject)
      .sort()
      .forEach(function(v, i) {
          console.log(v, "->", addressBookObject[v]);
       });

}

addressBook(['Tim:Doe Crossing', 'Bill:Nelson Place', 'Peter:Carlyle Ave', 'Bill:Ornery Rd']);