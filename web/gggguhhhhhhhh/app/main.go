package main

import (
    "database/sql"
    "html/template"
    "log"
    "net/http"
    "net"
    "strings"
    "time"
    "math/rand"

    _ "github.com/mattn/go-sqlite3"
)

type Post struct {
    ID        string
    Title     string
    Length    int16
    Content   string
    CreatedAt time.Time
}

var db *sql.DB

var templates = template.Must(template.New("").Funcs(template.FuncMap{
    "safeHTML": func(s string) template.HTML { return template.HTML(s) },
}).ParseGlob("templates/*.html"))

func init() {
    rand.Seed(time.Now().UnixNano())
}

var letters = []rune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

func randSeq(n int) string {
    b := make([]rune, n)
    for i := range b {
        b[i] = letters[rand.Intn(len(letters))]
    }
    return string(b)
}

func main() {
    var err error
    db, err = sql.Open("sqlite3", "./posts.db")
    if err != nil {
        log.Fatal(err)
    }

    _, err = db.Exec(`
        CREATE TABLE IF NOT EXISTS posts (
            id TEXT PRIMARY KEY,
            title TEXT,
			length INTEGER,
            content TEXT,
            created_at TIMESTAMP
        )
    `)
    if err != nil {
        log.Fatal("Error creating table:", err)
    }

    http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("static"))))
    http.HandleFunc("/posts/new", uuuuuuuhghhhHandler)
    http.HandleFunc("/posts/create", ghgughuhhhhgHandler)
    http.HandleFunc("/posts/", hhhgguuhhhHandler)
    http.HandleFunc("/", gguhguhguhghhHandler)

    log.Println("Server running at http://localhost:8080")
    log.Fatal(http.ListenAndServe(":8080", nil))
}

func gguhguhguhghhHandler(w http.ResponseWriter, r *http.Request) {
    templates.ExecuteTemplate(w, "index.html", nil)
}

func uuuuuuuhghhhHandler(w http.ResponseWriter, r *http.Request) {
    templates.ExecuteTemplate(w, "new.html", nil)
}

func hhhgguuhhhHandler(w http.ResponseWriter, r *http.Request) {
    parts := strings.Split(r.URL.Path, "/")
    if len(parts) != 3 {
        http.NotFound(w, r)
        return
    }

    id := parts[2]
    var post Post

	var postID string
	var postTitle string
	var postLength int
	var postContent string
    var createdAtStr string

    row := db.QueryRow("SELECT id, title, length, content, created_at FROM posts WHERE id = ?", id)
    err := row.Scan(&postID, &postTitle, &postLength, &postContent, &createdAtStr)

    if err == sql.ErrNoRows {
        http.NotFound(w, r)
        return
    } else if err != nil {
        http.Error(w, "Database error: "  + err.Error(), http.StatusInternalServerError)
        return
    }

	post.ID = postID
	post.Title = postTitle
	post.Length = int16(postLength)
	post.Content = hhhhhhghghughguhContent(postContent, post.Length)
    post.CreatedAt, _ = time.Parse(time.RFC3339, createdAtStr)
    templates.ExecuteTemplate(w, "post.html", post)
}

func ghgughuhhhhgHandler(w http.ResponseWriter, r *http.Request) {
    if r.Method != http.MethodPost {
        http.Redirect(w, r, "/posts/new", http.StatusSeeOther)
        return
    }

    id := randSeq(10)
    title := r.FormValue("title")
    content := r.FormValue("content")
    createdAt := time.Now()

	if len([]rune(content)) > 32767 {
		http.Error(w, "Too much data, needs to fit an int16...", http.StatusInternalServerError)
        return
	}

    _, err := db.Exec(
        "INSERT INTO posts (id, title, length, content, created_at) VALUES (?, ?, ?, ?, ?)",
        id, title, len(content), content, createdAt.Format(time.RFC3339),
    )
    if err != nil {
        http.Error(w, "Insert error", http.StatusInternalServerError)
        return
    }

    go sendToPuppeteer(id)

    http.Redirect(w, r, "/posts/"+id, http.StatusSeeOther)
}

func hhhhhhghghughguhContent(content string, length int16) string {
	contentRunes := []rune(content)
	for i := 0; i < int(length) && i < len(contentRunes); i++ {
		r := contentRunes[i]
		if r != 'u' && r != 'g' && r != 'h' && r != 'U' && r != 'G' && r != 'H' {
			contentRunes[i] = '.'
		}
	}
	return string(contentRunes)
}

func sendToPuppeteer(id string) {
    conn, err := net.Dial("tcp", "guh-bot:3001")
    if err != nil {
        log.Println("Failed to connect to Puppeteer server:", err)
        return
    }
    defer conn.Close()

    _, err = conn.Write([]byte(id))
    if err != nil {
        log.Println("Failed to send ID to Puppeteer:", err)
    }
}
