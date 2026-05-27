# Library Management System

A complete Python-based library management system that allows users to manage books, members, and book loans.

## Features

### 1. Add Book
- Add new books to the library
- Each book has a unique ID, title, and author
- Books are marked as "Available" when added

### 2. Register Member
- Register new library members
- Each member has a unique ID, name, and email
- Members can borrow and return books

### 3. Borrow Book
- Members can borrow available books
- Creates a loan record with loan ID, book, and member information
- Marks the book as unavailable during borrowing
- Error handling for:
  - Book not found
  - Member not found
  - Book already borrowed

### 4. Return Book
- Close an active loan and return the book
- Marks the book as available again
- Updates the return date on the loan record

### 5. View Books
- Display all books in the library
- Shows book ID, title, author, and availability status
- Status shows "Available" or "Borrowed"

### 6. View Members
- Display all registered members
- Shows member ID, name, and email

### 7. View Loans
- Display all loan transactions
- Shows loan ID, member name, book title, and status
- Status shows "Active" or "Closed"

### 8. Exit
- Gracefully close the application

## File Structure

```
.
├── book.py              # Book class definition
├── member.py            # Member class definition
├── loan.py              # Loan class definition
├── exceptions.py        # Custom exceptions
├── library_service.py   # LibraryService class with all operations
├── main.py              # Main application with CLI
└── README.md            # This file
```

## How to Run

```bash
python main.py
```

## Usage Example

```
1. Add a book:
   - Choose option 1
   - Enter Book ID: B001
   - Enter Book Title: Python Programming
   - Enter Book Author: Guido van Rossum

2. Register a member:
   - Choose option 2
   - Enter Member ID: M001
   - Enter Member Name: John Doe
   - Enter Member Email: john@example.com

3. Borrow a book:
   - Choose option 3
   - Enter Book ID: B001
   - Enter Member ID: M001
   - Loan ID: L001 is created

4. View all loans:
   - Choose option 7
   - See all active and closed loans

5. Return a book:
   - Choose option 4
   - Enter Loan ID: L001
   - Book is marked as available again
```

## Classes

### Book
- `book_id`: Unique identifier
- `title`: Book title
- `author`: Book author
- `available`: Boolean flag (True/False)

### Member
- `member_id`: Unique identifier
- `name`: Member name
- `email`: Member email

### Loan
- `loan_id`: Unique identifier (format: L001, L002, etc.)
- `book`: Reference to Book object
- `member`: Reference to Member object
- `borrow_date`: Date and time of borrowing
- `return_date`: Date and time of return (None if active)
- `is_active`: Boolean flag (True/False)

### LibraryService
Handles all CRUD operations for books, members, and loans.

## Error Handling

The system includes custom exceptions:
- `BookNotFoundError`: Raised when book is not found
- `MemberNotFoundError`: Raised when member is not found
- `BookUnavailableError`: Raised when book is already borrowed
- `InvalidInputError`: Raised for invalid input

## Data Structures

- **Books**: Dictionary `{book_id: Book}`
- **Members**: Dictionary `{member_id: Member}`
- **Loans**: List of Loan objects

## Design

The system follows the flowcharts provided:
1. Each operation follows its corresponding flowchart
2. Decision points handle validation and error cases
3. Clear separation of concerns between classes
4. Service layer handles business logic
5. CLI interface for user interaction

## Future Enhancements

- Persistent data storage (database or file)
- Search and filter functionality
- Due date tracking for borrowed books
- Fine calculation for overdue books
- Member dashboard
- Book recommendations
- User authentication
