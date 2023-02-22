class Keyword {
  constructor(mainKeyword) {
    this.mainKeyword = mainKeyword;
  }

  async getKeywords() {
    let keywords = [];
    let response = await fetch(`https://www.redbubble.com/shop/?query=${this.mainKeyword}`);
    let soup = new DOMParser().parseFromString(await response.text(), "text/html");
    let data = soup.getElementsByClassName('styles__box--2Ufmy styles__text--23E5U styles__display6--3wsBG styles__nowrap--33UtL styles__display-block--3kWC4');
    for (let i = 0; i < data.length; i++) {
      keywords.push(data[i].innerHTML);
    }
    return keywords;
  }
}

class DesignCount {
  constructor(mainKeyword) {
    this.mainKeyword = mainKeyword;
  }

  async getDesignCount() {
    let designCounts = [];
    let response = await fetch(`https://www.redbubble.com/shop/?query=${this.mainKeyword}`, {
      method: 'GET'
    });
    let soup = new DOMParser().parseFromString(await response.text(), "text/html");
    let data = soup.getElementsByClassName('styles__box--2Ufmy styles__text--23E5U styles__body--3StRc styles__muted--8wjeu');
    for (let i = 0; i < data.length; i++) {
      designCounts.push(data[i].innerHTML);
    }
    return designCounts;
  }
}

class AllFunction {
  constructor(mainKeyword) {
    this.mainKeyword = mainKeyword;
  }

  async addToMainList(key, universalList) {
    let obj = new DesignCount(key);
    try {
      let designCountInt = await obj.getDesignCount();
      let existingElement = document.getElemetById("myTable");
      command1 = `
          <div class="table-content" id="myTable">	
                <div class="table-row">		
                    <div class="table-data">${key}</div>
                    <div class="table-data">${designCountInt}</div>
                    <div class="table-data">hello</div>
                </div>
            </div>
          `
      existingElement.innerHTML += command1
    } catch (error) {
      console.log(`${keyword} failed`);
      process.exit();
    }
  }

  async mainFunction() {
    console.log('main function execution started');
    let universalList = [];
    let keywordObj = new Keyword(this.mainKeyword);
    let keywords = await keywordObj.getKeywords();
    for (let key of keywords) {
      await this.addToMainList(key, universalList);
    }
    console.log("exiting threading");
    return universalList;
  }
}

add_to_table = function () {

  console.log("hello word")
  // let mainObj = new AllFunction(query);
  // mainObj.mainFunction()
  let response = fetch('https://tools.wordstream.com/fkt?website=what&cid=&camplink=&campname=', {
    method: 'GET'
  })
  console.log(response.innerHTML())
}

add_alert = function () {
  alert("hello world")
}

//waste

function send() {

  console.log("tuleb siia");
  fetch("https://www.redbubble.com/shop/?query=hello&ref=search_box", {
    mode: 'no-cors',
    method: "GET",
    headers: {
      "Content-Type": "text/plain"
    },
  }).then(function (response) {
    return response.text();
  }).then(function (data) {
    console.log(data);
  });
}
send()


fetch("https://www.redbubble.com/shop/?query=hello&ref=search_box.example.com", {
  mode: 'no-cors',
  method: "GET",
})
  .then(response => response.text())
  .then(data => {
    const parser = new DOMParser();
    const doc = parser.parseFromString(data, "text/html");
    console.log(doc.body.innerHTML);
  })
  .catch(error => console.error("Error: ", error));