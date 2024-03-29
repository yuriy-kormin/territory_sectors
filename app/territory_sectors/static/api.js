async function getApiResponse(query){
    const csrftoken = getCookie('csrftoken');
    try {
      const response = await fetch('/graphql/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({query}),
      });
      const data = await response.json();
       return data['data']
    } catch (error) {
     console.error('Error:', error);
    }
}

async function get_sector_list(){
    const query = `
    query {
      sectorListing {
        id
        name
        updateHref
        uuid
        status
        historyHref
        assignedTo
        houses {
            address
            updateHref
            flatCount
        }
        removeHref
        statusAge
      }
    }
  `;
  const response = await getApiResponse(query)
  return response['sectorListing']
}

function statusRowColor(statusName){
    switch (statusName) {
        case "free":
            return "table-success";
        case "assigned":
            return "table-warning";
        case "under_construction":
            return "table-danger";
        case "completed":
            return "table-primary";
        default:
            return "";
    }
}
function createLink(href,text){
    let link = document.createElement('a');
    link.textContent = text;
    link.href = href;
    return link;
}

function createCellDiv(className){
    let cellDiv = document.createElement("div");
    cellDiv.classList.add(className);
    return cellDiv;
}

function createHouseListDiv(houseList){
    let rootDiv = document.createElement("div");
    houseList.forEach(function(house){
        const houseDiv = createCellDiv('row')
            let cellDiv =createCellDiv('col-12');
                const linkName = `${house['address']}(${house['flatCount']})`;
                let link = createLink(house['updateHref'],linkName);
                cellDiv.appendChild(link);
            houseDiv.appendChild(cellDiv);
        rootDiv.appendChild(houseDiv);
    })
    return rootDiv;
}
function createStatusDiv(name,info) {
    const rootDiv = createCellDiv('row')
        const nameDiv = createCellDiv('col-12')
        nameDiv.innerHTML = name
        rootDiv.appendChild(nameDiv)

        const infoDiv = createCellDiv('col-12')
        infoDiv.innerHTML = `<small>${info}</small>`
        rootDiv.appendChild(infoDiv)
    return rootDiv
}

function createRemoveSVG(){
    let svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
    svg.setAttribute("width", "16");
    svg.setAttribute("height", "16");
    svg.setAttribute("fill", "currentColor");
    svg.setAttribute("class", "bi bi-trash");
    svg.setAttribute("viewBox", "0 0 16 16");

    const path1 = document.createElementNS("http://www.w3.org/2000/svg", "path");
    path1.setAttribute("d", "M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5z");

    const path2 = document.createElementNS("http://www.w3.org/2000/svg", "path");
    path2.setAttribute("fill-rule", "evenodd");
    path2.setAttribute("d", "M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z");

    svg.appendChild(path1);
    svg.appendChild(path2);
    return svg;
}

function createRemoveButtonDiv(href){
    let rootDiv = document.createElement("div");
    const form = document.createElement("form");
    form.setAttribute("action", href);
    form.setAttribute("method", "GET");
        const submitBtn = document.createElement("button");
        submitBtn.classList.add("btn", "btn-outline-danger")
        submitBtn.setAttribute("button_type", "submit");
            const svg = createRemoveSVG()
            submitBtn.appendChild(svg)
        form.appendChild(submitBtn);
    rootDiv.appendChild(form);
    return rootDiv;
}

function clearTable(containerDiv){
  while (containerDiv.firstChild) {
    clearTable(containerDiv.firstChild);
    containerDiv.removeChild(containerDiv.firstChild);
  }
}

async function toggleSectorList() {
  var listDiv = document.getElementById("sectorList");
  var containerDiv = document.getElementById("sectorContainer");
  var toggleButton = document.getElementById("toggleButton");

  if (listDiv.style.display === "none") {
        const spinner = document.createElement("span");
          spinner.className = "spinner-border spinner-border-sm me-2";
          spinner.setAttribute("role", "status");
          spinner.setAttribute("aria-hidden", "true");
          toggleButton.innerHTML = "Loading.... ";
          toggleButton.appendChild(spinner);


    sectorList = await get_sector_list()
    sectorList.forEach(function(sector_json){
        //create row
        let rowDiv = document.createElement("div");
        rowDiv.classList.add("row","my-1","text-left", "align-middle");
        rowDiv.title=sector_json['uuid']
        const colorClass = statusRowColor(sector_json['status'])
        if (colorClass.trim() !== ""){rowDiv.classList.add(colorClass)}

            //create name col
            let cellDiv = createCellDiv("col-2")
                let link = createLink(sector_json['updateHref'],sector_json['name'])
                cellDiv.appendChild(link)
            rowDiv.appendChild(cellDiv);

            //create status col
            link = createLink(sector_json['historyHref'],sector_json['status'])
            cellDiv = createStatusDiv(link.outerHTML,`(${sector_json['statusAge']} месяцев)`)
            cellDiv.classList.add('col-3');
                rowDiv.appendChild(cellDiv);

            //create info(assigned_to) col
            cellDiv = createCellDiv("col-3")
                cellDiv.textContent = sector_json['assignedTo'];
                rowDiv.appendChild(cellDiv);

            //create houses col
            cellDiv = createHouseListDiv(sector_json['houses'])
            cellDiv.classList.add('col-3');
            rowDiv.appendChild(cellDiv);

            //create remove btn
            cellDiv = createRemoveButtonDiv(sector_json['removeHref'])
            cellDiv.classList.add('col-1');
            rowDiv.appendChild(cellDiv);

        containerDiv.appendChild(rowDiv)
    })
    listDiv.style.display = "block";
    toggleButton.innerHTML = "Hide List";
  } else {
    listDiv.style.display = "none";
    toggleButton.innerHTML = "Show List";
    clearTable(containerDiv)
  }
}

async function getPopupHTML(type,id) {
    let querytype = ''
    if (type === 'house') {
        querytype = 'houseById'
    } else if (type === 'sector') {
        querytype = 'sectorById'
    } else {
        return null
    }
    const query = `
            query {
              ${querytype}(id:${id}){
                popup
              }
            }
            `
    const response = await getApiResponse(query)
    if (response !== null) {
        return response[querytype]['popup']
    }
}