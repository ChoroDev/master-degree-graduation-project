let isFillRequest = [undefined, false, false, false, false, false, false, false, false]
let deleteElemIndex = [undefined, 1, 1, 1, 1, 1, 1, 1, 1]
let currentFillingElem = [undefined, 3, 3, 3, 3, 3, 3, 3, 3]
let emptyCounts = [undefined, 0, 0, 0, 0, 0, 0, 0, 0]
let fillIntervals = []
let products = [undefined,
  `<img src={% static 'images/apple.png' %} height=30>`,
  `<img src={% static 'images/pineapple.png' %} height=30>`,
  `<img src={% static 'images/carrot.png' %} height=30>`,
  `<img src={% static 'images/cucumber.png' %} height=30>`,
  `<img src={% static 'images/milk.png' %} height=30>`,
  `<img src={% static 'images/orange_juice.png' %} height=30>`,
  `<img src={% static 'images/potato.png' %} height=30>`,
  `<img src={% static 'images/tomato.png' %} height=30>`,
]
let productsCountInStore = [undefined,
  JSON.parse("{{ storeProducts|escapejs }}")[0].fields.product_count,
  JSON.parse("{{ storeProducts|escapejs }}")[1].fields.product_count,
  JSON.parse("{{ storeProducts|escapejs }}")[4].fields.product_count,
  JSON.parse("{{ storeProducts|escapejs }}")[5].fields.product_count,
  JSON.parse("{{ storeProducts|escapejs }}")[3].fields.product_count,
  JSON.parse("{{ storeProducts|escapejs }}")[2].fields.product_count,
  JSON.parse("{{ storeProducts|escapejs }}")[6].fields.product_count,
  JSON.parse("{{ storeProducts|escapejs }}")[7].fields.product_count,
]
let productsCountInStorage = [undefined,
  JSON.parse("{{ storageProducts|escapejs }}")[0].fields.product_count,
  JSON.parse("{{ storageProducts|escapejs }}")[1].fields.product_count,
  JSON.parse("{{ storageProducts|escapejs }}")[4].fields.product_count,
  JSON.parse("{{ storageProducts|escapejs }}")[5].fields.product_count,
  JSON.parse("{{ storageProducts|escapejs }}")[3].fields.product_count,
  JSON.parse("{{ storageProducts|escapejs }}")[2].fields.product_count,
  JSON.parse("{{ storageProducts|escapejs }}")[6].fields.product_count,
  JSON.parse("{{ storageProducts|escapejs }}")[7].fields.product_count
]
let isReady = [undefined, true, true, true, true, true, true, true, true]


window.addEventListener('load', () => {
  for (let i = 1; i < 9; i++) {
    let currentProductsInShelf = productsCountInStore[i]
    let shelf = document.getElementById('shelf' + i)
    if (currentProductsInShelf < 9) {
      for (let j = 1; j < 11 - currentProductsInShelf; j++) {
        shelf.childNodes.item(j * 2 - 1).innerHTML = ""
        deleteElemIndex[i] += 2
        emptyCounts[i]++
      }
      emptyCounts[i]--
      deleteElemIndex[i] -= 2
    }
    shelf.childNodes.forEach(element => {
      element.style = 'animation: none;'
    })
    fillIntervals[i] = setInterval(() => {
      if (emptyCounts[i] > 5) {
        clearInterval(fillIntervals[i])
        fillShelf('shelf' + i)
      }
    })
    let shelfFiller = document.getElementById('shelf_up' + i)
    shelfFiller.style = 'left: -85px'
    shelfFiller.childNodes.forEach(element => {
      element.style = 'animation: none;'
    })
  }
})


function fillShelf(shelfId) {
  isReady[shelfId.slice(-1)] = false
  isFillRequest[shelfId.slice(-1)] = true
  fillIntervals[shelfId.slice(-1)] = setInterval(() => {
    let takeButton = document.getElementById('take-button' + shelfId.slice(-1))
    takeButton.innerHTML = 'Filling<br>wait...<br>🡄◼◼◼'
    takeButton.disabled = true
    fill(shelfId)
  }, 1000)
}


function take(shelfId) {
  let elementsTook = 1
  let shelf = document.getElementById(shelfId)
  if (isReady[shelfId.slice(-1)] && emptyCounts[shelfId.slice(-1)] < 9) {
    isReady[shelfId.slice(-1)] = false
    let lastChild = shelf.childNodes.item(shelf.childNodes.length - 2)
    let animationEnd = () => {
      shelf.childNodes.item(deleteElemIndex[shelfId.slice(-1)]).innerHTML = ""
      lastChild.innerHTML = products[shelfId.slice(-1)]
      if (emptyCounts[shelfId.slice(-1)] == 9) {
        lastChild.innerHTML = ``
      }
      isReady[shelfId.slice(-1)] = true
      lastChild.removeEventListener('animationend', animationEnd)
    }
    let animationEndGeneric = (event) => {
      event.currentTarget.style = 'animation: none;'
      event.currentTarget.removeEventListener('animationend', animationEndGeneric)
    }

    lastChild.innerHTML = ''
    lastChild.addEventListener('animationend', animationEnd)
    shelf.childNodes.forEach(element => {
      element.style = 'animation: ""; animation-iteration-count: ' + elementsTook + ';'
      element.addEventListener('animationend', animationEndGeneric)
    })

    deleteElemIndex[shelfId.slice(-1)] += 2
    emptyCounts[shelfId.slice(-1)]++
  } else if (isReady[shelfId.slice(-1)]) {
    fillShelf(shelfId)
  }
}


function fill(shelfId) {
  let takeButton = document.getElementById('take-button' + shelfId.slice(-1))
  let elementsGave = 1
  let shelfUpId = 'shelf_up' + shelfId.slice(-1)
  let shelfFiller = document.getElementById(shelfUpId)
  if (isReady[shelfId.slice(-1)] && emptyCounts[shelfId.slice(-1)] > 0) {
    isReady[shelfId.slice(-1)] = false
    let firstChild = shelfFiller.childNodes.item(currentFillingElem[shelfId.slice(-1)])
    let animationEnd = () => {
      firstChild.innerHTML = products[shelfId.slice(-1)]
      isReady[shelfId.slice(-1)] = true
      firstChild.removeEventListener('animationend', animationEnd)
    }
    let animationEndGeneric = (event) => {
      event.currentTarget.style = 'animation: none;'
      event.currentTarget.removeEventListener('animationend', animationEndGeneric)
    }

    firstChild.addEventListener('animationend', animationEnd)
    shelfFiller.childNodes.forEach(element => {
      element.style = 'animation: ""; animation-iteration-count: ' + elementsGave + ';'
      element.addEventListener('animationend', animationEndGeneric)
    })
    currentFillingElem[shelfId.slice(-1)] += 2
    emptyCounts[shelfId.slice(-1)]--
  } else if (emptyCounts[shelfId.slice(-1)] > 0 && isFillRequest[shelfId.slice(-1)]) {
    isFillRequest[shelfId.slice(-1)] = false
    isReady[shelfId.slice(-1)] = true
  } else if (isReady[shelfId.slice(-1)]) {
    clearInterval(fillIntervals[shelfId.slice(-1)])
    deleteElemIndex[shelfId.slice(-1)] = 1
    currentFillingElem[shelfId.slice(-1)] = 3
    let shelf = document.getElementById(shelfId)
    shelf.childNodes.forEach(element => {
      element.innerHTML = products[shelfId.slice(-1)]
    })
    shelfFiller.childNodes.forEach(element => {
      element.innerHTML = ''
    })
    fillIntervals[shelfId.slice(-1)] = setInterval(() => {
      if (emptyCounts[shelfId.slice(-1)] > 5) {
        clearInterval(fillIntervals[shelfId.slice(-1)])
        fillShelf(shelfId)
      }
    })
    takeButton.innerHTML = 'Take<br>🡄◼◼◼'
    takeButton.disabled = false
  }
}
