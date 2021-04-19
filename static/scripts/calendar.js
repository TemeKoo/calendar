function save() {
    if (this.innerHTML.length > 0) {
        localStorage.setItem(this.id, this.innerHTML);
    } else {
        localStorage.removeItem(this.id)
    }
}

function addSaveListeners() {
    var textboxes = document.getElementsByClassName("day-text");

    for (let item of textboxes) {
        item.addEventListener("blur", save);
    }
}

function retrieve() {
    var textboxes = document.getElementsByClassName("day-text");

    for (let item of textboxes) {
        let stored = localStorage.getItem(item.id)
        if (stored !== null) {
            item.innerHTML = stored
        }
    }
}