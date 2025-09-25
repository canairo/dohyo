const puppeteer = require('puppeteer')
const net = require('net')


const genRanHex = size => [...Array(size)].map(() => Math.floor(Math.random() * 16).toString(16)).join('');

const BASE_URL = process.env.BASE_URL || 'http://guh-app:8080/posts/'
const FLAG = 'DOHYO{' + genRanHex(32) + '}'

const browserPool = []

const getBrowser = async () => {
    if (browserPool.length > 0) {
        return browserPool.pop()
    }
    return await puppeteer.launch({
        headless: true,
        args: ['--js-flags=--jitless', '--no-sandbox', '--disable-setuid-sandbox']
    })
}

const returnBrowser = (browser) => {
    browserPool.push(browser)
}

const visitSubmission = async (id) => {
    if (!id.match(/^[0-9a-zA-Z]{10}$/)) {
        return
    }
    const browser = await getBrowser()
    const page = await browser.newPage()
    const hostname = new URL(BASE_URL).hostname
    await page.setCookie({
        name: 'admin_flag',
        value: FLAG,
        domain: hostname,
        path: '/',
        httpOnly: false,
        secure: false
    })
    try {
        await page.goto(BASE_URL + id, { waitUntil: 'networkidle2', timeout: 5000 })
    }
    catch (e) {
        console.log(e)
    }
    await page.close()
    console.log(`visited ${BASE_URL + id}`)
    returnBrowser(browser)
}

setInterval(() => {
    while (browserPool.length > 0) {
        const browser = browserPool.pop()
        browser.close()
    }
}, 5 * 60 * 1000)

const server = net.createServer((socket) => {
    socket.on('data', async (data) => {
        const id = data.toString()
        console.log(`visiting ${id}`)
        await visitSubmission(id)
    })
})

server.listen(3001, () => {
    console.log('Listening on port 3001')
})                                                                                                            
