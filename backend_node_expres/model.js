const sqlite3 = require('sqlite3').verbose()

const db = new sqlite3.Database('./db/books.db', sqlite3.OPEN_READWRITE, (err) => {
    if (err) {
        console.error(err.message)
        throw err
    }
    console.log('Connected to the books database')
})

const getBooks = (responseHandler) => {
    db.all('SELECT * FROM books;', (err, rows) => {
        if (err) console.error(err.message)
        responseHandler(rows)
    })
}

const createBook = (values, responseHandler) => {
    // values= {
    //     title: 'Harry potter',
    //     author: 'JKR'
    // }
    const { title, author } = values

    db.run('INSERT INTO books (title, author) VALUES (?, ?);', [title, author], (err) => {
        if (err) console.error(err.message)
        responseHandler()
    })
}

module.exports = { getBooks, createBook }
