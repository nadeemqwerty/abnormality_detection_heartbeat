import React from 'react';

function Murmur(props) {
    return (
        <div style={props.style.main}>
            <header style={props.style.header}>
                Murmur
            </header>
            <body style={props.style.body}>
                <b>You belong to Murmur class with a probability score of :-- {props.val}</b>
                <br/>
                Heart murmurs sound as though there is a “whooshing, roaring, rumbling, or turbulent fluid” noise in one of two temporal locations: (1) between “lub” and “dub”, or (2) between “dub” and “lub”. They can be a symptom of many heart disorders, some serious. There will still be a “lub” and a “dub”. One of the things that confuses non-medically trained people is that murmurs happen between lub and dub or between dub and lub; not on lub and not on dub.(source: Rita Getz)
            </body>
        </div>
    )
}

export default Murmur;