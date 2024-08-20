export default function Equipment() {

    // where should I use state?

    const listOfUsedEquipment = ["Loggers", "Machines", "Electronics", "Meters"];

    const eqSampleData1 = {
        name: "Machine 1",

    };

    // array of data for rendering:
    const people = [
        'Creola Katherine Johnson: mathematician',
        'Mario José Molina-Pasquel Henríquez: chemist',
        'Mohammad Abdus Salam: physicist',
        'Percy Lavon Julian: chemist',
        'Subrahmanyan Chandrasekhar: astrophysicist'
    ];

    const listItems = people.map( v => <li>{v}</li>)

    return (<>
        <p>Here will b e the equipment mapped:</p>
        <ul>
            {/* Here I am feeding the program with the items I've mentioned above */}
            {listItems}
        </ul>
    </>)

}