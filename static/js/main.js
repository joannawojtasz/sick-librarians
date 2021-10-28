
var collapseElementList = [].slice.call(document.querySelectorAll('.collapse'))
    var collapseList = collapseElementList.map(function (collapseEl) {
        return new bootstrap.Collapse(collapseEl)
    })

// get all the start

    const one = document.getElementById('first')
    const two = document.getElementById('second')
    const three = document.getElementById('third')
    const four = document.getElementById('fourth')
    const five = document.getElementById('fifth')

    const form = document.querySelector('.rate-form')
    const confirmBox = document.getElementById('confirm-box')

    const csrf = document.getElementsByName('csrfmiddlewaretoken')

    const handleStarSelect = (size) => {
        const children = form.children
        for (let i=0; i < children.length; i++) {
            if( i <= size) {
                children[i].classList.add('checked');
            } else {
                children[i].classList.remove('checked');
            }
        }
    }

    handleStarSelect(4)
    
    const handleSelect = (selection) => {
        switch(selection){
            case 'first': {
                // one.classList.add('checked')
                // two.classList.remove('checked')
                // three.classList.remove('checked')
                // four.classList.remove('checked')
                // five.classList.remove('checked')
                handleStarSelect(1)
                return
            }
            case 'second': {
                handleStarSelect(2)
                return
            }
            case 'third':
            {
                handleStarSelect(3)
                return
            }
            case 'fourth':
            {
                handleStarSelect(4)
                return
            }
            case 'fifth':
            {
                handleStarSelect(5)
                return
            }
        }
    }

    const arr = [one, two, three, four, five]

    arr.forEach(item=>
    item.addEventListener("mouseover", (event)=>{
        console.log(event.target)
    }))