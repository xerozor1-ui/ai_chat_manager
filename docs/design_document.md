# Week 1 Lab: Understanding the Problem

**Project:** AI Chat Manager  
**Reference:** AI Chat Manager — Project Concept Document

## Part 1: Document Comprehension

### 1. What problem does the AI Chat Manager solve? Who experiences this problem?

The AI Chat Manager helps people find useful information buried in their past AI conversations. Someone might solve a technical problem or develop an idea with an AI assistant, then have trouble finding that conversation later because it is mixed in with hundreds of other chats or stored on another platform. The application brings those conversations into one organized, searchable system. This would help professionals, students, researchers, and anyone who regularly uses AI assistants.

### 2. List the five core capabilities the finished system will provide.

1. **Chat Import and Organization:** Bring in exported conversations, extract their information, and organize them with categories and tags.
2. **Search and Retrieval:** Find conversations using keywords, dates, topics, and natural language queries, with enough surrounding context to understand the results.
3. **AI-Powered Analysis:** Answer questions about saved conversations, summarize related discussions, and identify common themes using AI and RAG.
4. **Automation and Agents:** Watch selected folders, process new exports automatically, and perform routine organization through configurable workflows.
5. **User Interface:** Provide a browser-based interface with a dashboard for browsing, searching, and reviewing activity on desktop or mobile devices.

### 3. Why does the project use a phased approach rather than building everything at once?

Building in phases makes the project easier to manage and troubleshoot. Course 1 establishes how chat sessions are added, stored, listed, and searched in a command-line application. Course 2 builds on that foundation with a web interface, database, and deployment infrastructure. Course 3 adds AI, RAG, and automated processing. This approach allows the basic functions to be checked before more complicated features depend on them, while extending the same codebase throughout the project.

### 4. What is RAG, and how will it be used in this system?

RAG stands for **Retrieval-Augmented Generation**. The system first searches stored information for content relevant to a user's question, then gives that content to the language model as context for its answer. In the AI Chat Manager, that information comes from the user's saved conversations. For example, someone could ask what solution they previously discussed for a technical issue, and the system could retrieve that discussion to help answer. This grounds the response in the stored history, although it does not guarantee that every generated answer is correct.

### 5. Who are the target users for this application? Name at least two types.

- **Professionals:** People who need to retrieve past troubleshooting steps, work drafts, or project decisions.
- **Students:** People who want to revisit explanations and organize study conversations.
- **Researchers:** People who need to organize and connect ideas discussed across multiple sessions.
- **Other regular AI users:** Anyone who wants an easier way to manage and search their conversation history.

## Part 2: From Concept to Requirements

**Concept:** “The system monitors designated folders for new chat exports.”

The requirements below are proposed choices for this exercise. The concept document does not specify a detection interval or supported import formats. The 60-second target and JSON/plain-text support would need confirmation before implementation.

### Derived Requirement 1: Configure the monitored folders

**The system shall allow users to add and remove monitored folder paths, verify that each added folder exists and is readable, and save the accepted paths for future runs.**

**Reasoning:** “Designated folders” means the system needs to know which locations the user has selected. Checking access prevents a folder from appearing to be monitored when it cannot be read. Saving the settings avoids requiring the user to enter the paths every time the application starts.

### Derived Requirement 2: Detect new exports automatically

**While monitoring is enabled and the application is running, the system shall detect a newly added, fully written, readable JSON or plain-text export in a configured folder and queue it for processing within 60 seconds.**

**Reasoning:** Monitoring should happen without the user manually checking for files. A measurable time limit makes it possible to verify that detection works. Requiring the file to be fully written prevents processing an incomplete export while it is still being copied. This target covers detection and queuing, not completion of the import.

### Derived Requirement 3: Validate detected files

**The system shall validate queued files against the supported chat-export structure before importing them, skip unsupported or invalid files, and record the filename and reason for each skipped file without stopping folder monitoring.**

**Reasoning:** A file ending in `.json` or `.txt` is not necessarily a usable chat export. Validation prevents unrelated or malformed content from becoming a chat session. Recording the reason helps the user correct a failed import while allowing other files to continue processing.

## Part 3: Practice Decomposition

These sub-requirements propose initial behavior for the application. Details such as the name limit, date format, matching rules, and ranking order are design choices for this exercise rather than rules already established by the concept document.

### Requirement 1: Add new chat sessions manually

**Parent requirement:** “The system shall allow users to add new chat sessions manually.”

1. **Session name:** The system shall request a session name, remove leading and trailing whitespace, and require the resulting name to contain between 1 and 100 characters.
2. **Session date:** The system shall accept a valid calendar date in `YYYY-MM-DD` format and use the current local date when the user leaves the date blank.
3. **Conversation content:** The system shall accept multiline conversation text, require at least one non-whitespace character, and preserve the entered text and line order.
4. **Optional tags:** The system shall accept optional comma-separated topic tags, trim surrounding whitespace from each tag, and discard empty tags and case-insensitive duplicates.
5. **Persistent storage:** After the input passes validation, the system shall assign a unique session identifier and save the name, date, conversation content, and tags in local JSON storage so the session remains available after restarting the application.
6. **User feedback:** The system shall identify invalid input so the user can correct it, report a storage failure without claiming success, and display the session name and identifier as confirmation only after a successful save.

Together, these steps cover collecting the required information, validating it, storing the session, and telling the user whether the operation succeeded.

### Requirement 2: Search stored sessions and rank results

**Parent requirement:** “The system shall allow users to search across all stored chat sessions and return results ranked by relevance.”

1. **Query input:** The system shall accept a search query, remove leading and trailing whitespace, and request a new query if the result is empty.
2. **Search scope and matching:** The system shall search every stored session's name, topic tags, and conversation content using case-insensitive matching. For this initial version, the entire trimmed query shall be treated as a literal phrase that may appear anywhere within one of those fields.
3. **Relevance ranking:** The system shall rank name matches first, tag matches second, and conversation-content matches third. A session matching more than one field shall appear once in its highest applicable group. Ties shall be ordered by session date from newest to oldest, then by session identifier in ascending order.
4. **Result display:** The system shall show each matching session's identifier, name, date, and tags, together with an excerpt of up to 200 characters from the matching field that includes the start of the match. The matching field shall be labeled so the user understands why the session was returned.
5. **Full-session access:** The system shall allow the user to select a result by its identifier and view the complete stored conversation and metadata.
6. **No-match handling:** When no sessions match, the system shall display “No sessions found matching your search” and allow the user to enter another query. An empty collection shall instead display “No saved sessions to search.”

This provides a simple, predictable relevance rule for the early application. Natural language retrieval can be added in the later AI phase.

## Part 4: Identify Missing Requirements

### Scenario 1: “Users can search sessions by keyword.”

1. Which fields should the search include: session names, tags, conversation content, or all three?
2. Should matching ignore capitalization, and should it accept partial words or require complete words?
3. If the user enters multiple words, should results contain every word, any word, or the exact phrase?

### Scenario 2: “The system automatically categorizes imported chat sessions.”

1. Where do the categories come from: a fixed list, categories created by the user, or categories generated from the conversations?
2. Can a conversation belong to multiple categories when it covers more than one subject?
3. What should happen when the system is uncertain or assigns the wrong category, and how will a user's correction be preserved during later processing?

### Scenario 3: “Users can export their organized chat data.”

1. Which output formats must the system support, such as JSON, CSV, or plain text?
2. Can users export individual sessions, a filtered group, and their entire collection?
3. What must the export contain—full conversations, dates, tags, categories, and identifiers—and can the user choose what to include?

## Part 5: Reflection

*These first-person reflections are drafts to review and personalize to match your experience.*

### 1. How did reading the concept document first help you understand what you would be building?

Reading the concept document helped me understand the purpose of the application before focusing on individual features. The main goal is to make information from past AI conversations easier to find and use. It also showed how the three courses fit together, so I could see why the first command-line version needs a solid approach to storing and searching sessions.

### 2. What was challenging about breaking large requirements into smaller pieces? What made it easier?

The challenging part was recognizing how much is hidden inside a simple requirement like “add a session.” It needs more than an input field; the application also needs validation, storage, and clear feedback. Walking through the process from the user's first action to the saved result made it easier to identify each step and notice what could go wrong.

### 3. When you identified missing information in Part 4, what types of questions came to mind first? What does this tell you about what you consider important?

The first questions I focused on were what information the system should use and how it should handle unclear or incorrect input. For example, keyword search could behave very differently depending on whether it searches only titles or the entire conversation. This shows that I value predictable results and clear rules, because users need to understand what the system is doing and trust that it works consistently.

### 4. If you were given a concept document for a different project tomorrow, what would you do differently after completing this lab?

I would first identify the problem, the intended users, and what a successful result should look like. Then I would walk through each major feature, break it into smaller actions, and separate confirmed requirements from assumptions that need clarification. I would also look for missing error handling and decide how each requirement could be checked before starting to code.
