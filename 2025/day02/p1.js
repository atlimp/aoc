import { readFileSync } from 'fs';

async function main() {
    const buffer = readFileSync('input', 'utf8');
    const productIds = buffer.split(',');
    
    let sum = 0;
    for (let id of productIds) {
        const [start, end] = id.split('-').map(Number);
        
        for (let i = start; i <= end; i++) {
            const idStr = `${i}`;
            const midpoint = Math.floor(idStr.length / 2);
            const p1 = idStr.substring(0, midpoint);
            const p2 = idStr.substring(midpoint);

            if (p1 === p2) {
                console.log('match', i);
                sum += i;
            }
        }
    }

    console.log(sum);
}

main();