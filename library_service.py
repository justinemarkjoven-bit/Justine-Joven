"""LibraryService class that handles all library operations."""

from book import Book
from member import Member
from loan import Loan
from exceptions import BookNotFoundError, MemberNotFoundError, BookUnavailableError


class LibraryService:
    """Service class for managing library operations."""

    def __init__(self):
        """Initialize the library service with empty data structures."""
        self._books = {}  # Dictionary to store books {book_id: Book}
        self._members = {}  # Dictionary to store members {member_id: Member}
        self._loans = []  # List to store loans
        self._loan_counter = 0  # Counter for generating loan IDs

    def add_book(self, book_id, title, author):
        """
        Add a new book to the library.

        Args:
            book_id (str): Unique identifier for the book
            title (str): Title of the book
            author (str): Author of the book

        Returns:
            str: Success message
        """
        if book_id in self._books:
            return f"Book with ID {book_id} already exists."

        book = Book(book_id, title, author)
        self._books[book_id] = book
        return f"Book added: {title}"

    def register_member(self, member_id, name, email):
        """
        Register a new member in the library.

        Args:
            member_id (str): Unique identifier for the member
            name (str): Name of the member
            email (str): Email address of the member

        Returns:
            str: Success message
        """
        if member_id in self._members:
            return f"Member with ID {member_id} already exists."

        member = Member(member_id, name, email)
        self._members[member_id] = member
        return f"Member registered: {name}"

    def borrow_book(self, book_id, member_id):
        """
        Borrow a book from the library.

        Args:
            book_id (str): ID of the book to borrow
            member_id (str): ID of the member borrowing

        Returns:
            str: Success message

        Raises:
            BookNotFoundError: If book is not found
            MemberNotFoundError: If member is not found
            BookUnavailableError: If book is already borrowed
        """
        # Lookup book
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError("Book not found.")

        # Lookup member
        member = self._members.get(member_id)
        if member is None:
            raise MemberNotFoundError("Member not found.")

        # Check book availability
        if not book.available:
            raise BookUnavailableError("Book is already borrowed.")

        # Borrow the book
        book.borrow()

        # Create and store loan
        self._loan_counter += 1
        loan_id = f"L{self._loan_counter:03d}"
        loan = Loan(loan_id, book, member)
        self._loans.append(loan)

        return f"{member.name} borrowed {book.title}"

    def return_book(self, loan_id):
        """
        Return a borrowed book to the library.

        Args:
            loan_id (str): ID of the loan to close

        Returns:
            str: Success message

        Raises:
            Exception: If loan is not found or already closed
        """
        for loan in self._loans:
            if loan.loan_id == loan_id:
                if not loan.is_active:
                    return f"Loan {loan_id} is already closed."

                # Return the book
                loan.book.return_book()
                loan.close_loan()
                return f"{loan.member.name} returned {loan.book.title}"

        raise Exception(f"Loan {loan_id} not found.")

    def view_books(self):
        """
        Get a list of all books in the library.

        Returns:
            list: List of Book objects
        """
        return list(self._books.values())

    def view_members(self):
        """
        Get a list of all members in the library.

        Returns:
            list: List of Member objects
        """
        return list(self._members.values())

    def view_loans(self):
        """
        Get a list of all loans.

        Returns:
            list: List of Loan objects
        """
        return list(self._loans)

    def get_book(self, book_id):
        """
        Get a specific book by ID.

        Args:
            book_id (str): ID of the book

        Returns:
            Book: The book object or None if not found
        """
        return self._books.get(book_id)

    def get_member(self, member_id):
        """
        Get a specific member by ID.

        Args:
            member_id (str): ID of the member

        Returns:
            Member: The member object or None if not found
        """
        return self._members.get(member_id)