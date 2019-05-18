import React from 'react';

function Extrasystole(props) {
    return (
        <div style={props.style.main}>
            <header style={props.style.header}>
                Extrasystole
            </header>
            <body style={props.style.body}>
                <b>You belong to Extrasystole class with a probability score of :-- {props.val}</b>
                <br/>
                Extrasystole sounds may appear occasionally and can be identified because there is a heart sound that is out of rhythm involving extra or skipped heartbeats, e.g. a “lub-lub dub” or a “lub dub-dub”. (This is not the same as an extra heart sound as the event is not regularly occuring.) An extrasystole may not be a sign of disease. It can happen normally in an adult and can be very common in children. However, in some situations extrasystoles can be caused by heart diseases. If these diseases are detected earlier, then treatment is likely to be more effective. (source: Rita Getz)
            </body>
        </div>
    )
}

export default Extrasystole;