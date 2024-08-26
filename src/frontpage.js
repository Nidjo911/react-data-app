import './frontpage.css';
import { useState } from 'react';

export default function Front() {

    const [index, setIndex] = useState(0);
    const [showMore, setShowMore] = useState(false);


    return (

        <main>
            <h1>Mediterranian sea beauty meets forest!</h1>

            <span>{index}</span>
            <span>{showMore}</span>
            <p>Welcome camping in most heavenly place! Enjoy the peace and get rest.</p>

        </main>
    )
}