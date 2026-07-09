
53
Summary
During  my  industrial  training  at  the  Faculty  of  Computing,  Universiti 
Teknologi  Malaysia,  I  was  assigned  a  major  software  development  task  titled:  ”AI-
POWERED  HELPDESK  CHATBOT  FOR  FC  INTERNAL  QUALITY 
ASSURANCE  (IQA)”  This  project  involved  building  an  intelligent system  capable 
of  answering  user  queries  based  on  the  content  of  uploaded  PDF documents, such 
as technical manuals or internal reports.
The primary objectives of this project were:
• To  design  and  implement  a  user-friendly  chatbot  interface  with  real-time 
response capabilities.
• To  build  a  full-stack  system  that  handles  PDF  upload,  chunking,  semantic 
embedding, and similarity search.
• To integrate local and cloud-based AI models via Ollama for natural language 
processing and inference.
• To  implement  user  role  management  (Visitor,  Admin,  System  Admin)  for 
secured access and dashboard control.
• To maintain chat history, handle multi-turn conversation threads, and support 
document-aware Q&A.
The technical work involved full-stack development using React.js (frontend),
Express.js with Node.js (backend), MongoDB Atlas (database), and Tailwind CSS
for the UI. PDF parsing was done using pdf-parse, and semantic chunking was
achieved through a custom JavaScript function that created overlapping word blocks.
Each chunk was then embedded using the all-MiniLM embedding model served
locally via Ollama. These embeddings were stored in MongoDB, allowing the system
to retrieve semantically similar chunks using cosine similarity.
The chatbot was developed as a modular and scalable application, integrating
advanced NLP components. A well-defined pipeline ensured that only the most
relevant context was sent to the language model, reducing latency and improving
28
answer accuracy. Furthermore, a Gantt chart was followed to ensure timely delivery of
each milestone—from interface design to final deployment.
Challenges such as embedding inconsistency, LLM response latency, and chat
history bugs were handled using debouncing techniques, caching, and code refactoring.
The system was tested using manual black-box testing, Postman API checks, and
frontend simulations across different browsers.
Overall, this chapter presents a technical deep dive into the construction of
an AI chatbot capable of serving industrial Q&A use cases in a real-world academic
setting.
29
CHAPTER 3
OVERALL INFORMATION OF THE INDUSTRIAL TRAINING
3.1 Lessons Learned from Supervisor, Personal, and Resources
From Supervisor
My supervisor consistently emphasized writing clean, maintainable code and
the importance of code reviews.
• I learned to maintain a modular structure, document my work clearly, and
ensure that the system was user-centric in terms of UX.
• They also guided me on debugging critical issues using logging tools, browser
developer tools, and asynchronous error handling in Node.js.
My Technical Workflow
• I worked in a version-controlled environment using GitHub, where I applied
branching strategies to isolate features and fixes, resolved merge conflicts, and
followed clear commit conventions like feat:, fix:, and chore:.
• Weekly syncs helped me maintain an agile flow—planning tasks in short
sprints, presenting updates through demos, and organizing my progress using
a task board.
• I made use of MongoDB for storing data efficiently and designed RESTful
APIs using scalable patterns to ensure stability and growth over time.
31
From Tools and References
• Ollama CLI: Learned how to run and manage local LLMs like mistral, pull
embedding models (all-minilm), and connect them via HTTP API.
– ollama pull all-minilm
– ollama run mistral
• Mongoose Indexing: Discovered that adding indexes (e.g., on userId,
createdAt) drastically improved query speed and response times during chat
search.
– chatSchema.index({userId: 1, createdAt: -1
});
• Axios Retry & Timeout Handling: Implemented robust retry logic for LLM
calls to handle timeout failures using tools like axios-retry.
– const axiosRetry = require(’axios-retry’);
– axiosRetry(axios, {retries: 3, retryDelay:
axiosRetry.exponentialDelay });
• Framer Motion & Tailwind CSS: Improved UI aesthetics with motion
transitions and responsive dark-themed layouts. I learned how to balance
animation with performance.
3.2 Comments on Overall Task Performance
Throughout the training, I was able to:
32
Task Area Comment
PDF Upload & Parsing Delivered a fast and error-tolerant module using
pdf-parse.
Chunking & Embedding Optimized chunking logic with semantic over-
lap for higher relevance.
Chat History System Refactored to prevent empty threads and added
rename/delete features.
Frontend Integration Built responsive React components with load-
ing states, chat stream, and animated sidebar.
Backend Services Handled all API logic with clean controllers,
route protection, and DB queries using Mon-
goose.
Testing & Debugging Covered all key flows using Postman, browser
dev tools, and console-based tracing.
Table 3.1 Performance Overview Across Key Development Areas
I was able to complete all planned features within the expected timeframe while
maintaining code readability, performance, and functionality. My supervisor noted
improvements in my debugging speed, attention to detail, and ability to self-solve
complex integration issues.
Summary
My industrial training experience was highly enriching, offering deep exposure
to real-world full-stack development, AI integration, and teamwork in a semi-research
academic environment.
One of the most valuable aspects of this training was the guidance I received
from my supervisor. Through regular code reviews and discussions, I learned how
33
to maintain clean code practices, follow semantic version control, and adopt a user-
centered design approach.
Working with peers and the technical staff within the lab, I experienced
collaborative Git workflows, including resolving merge conflicts, managing parallel
branches, and coordinating code pushes on GitHub. These experiences significantly
improved my team communication and planning skills, especially when aligning tasks
with a project Gantt chart.
From the tools I used, I gained hands-on experience with:
• Ollama CLI for running and testing large language models (LLMs) locally.
• MongoDB Atlas for efficient storage and querying of vector embeddings.
• Vite + React stack for frontend development and hot-reload interface testing.
• Postman and custom scripts for validating backend endpoints.
I also improved my understanding of AI-specific tools like embedding models
(all-MiniLM), prompt engineering, and building intelligent fallback strategies for
LLM queries.
The overall project helped me grow technically and professionally. It
challenged me to think about user experience, scalability, and deployment-readiness
while still maintaining code that is readable, testable, and maintainable. I also became
more confident in navigating complex systems, isolating bugs, and writing clear
documentation for both users and future developers.
34
CHAPTER 4
CONCLUSION
4.1 Overall Achievement of the Industrial Training
During the 8-week industrial training program at the Faculty of Computing,
Universiti Teknologi Malaysia, I successfully designed, developed, and deployed
an AI-Powered Industrial Q&A Chatbot system. My work spanned full-stack
development, artificial intelligence integration, real-time chat systems, and user role
management.
Here’s a summary of what was accomplished:
• Built a full-stack web app using React, Node.js, MongoDB, Tailwind CSS, and 
Framer Motion.
• Enabled  intelligent  PDF  understanding  through  Ollama and its Local 
LLMs.
• Used all-MiniLM embeddings for vector similarity search.
• Implemented user roles (Visitor, Admin, System Admin) and protected route 
access.
• Added chat history features:  rename, delete, persist chat threads, and prevent 
empty chats.
• Developed a New  Chat button flow that only saves completed conversations.
• Enabled chunk-based semantic search with PDF text parsing and indexing.
• Ran  a  local  development  environment  with  .env  configuration,  Postman 
testing, and Ollama integration.
35
This project not only met all functional objectives but also improved
performance, relevance, and UI usability. The chatbot was successfully able to answer
industrial questions based on uploaded documents, which reflects the original vision
of the system.
4.2 Problems Faced and How I Solved Them
Problem Solution
Embedding inconsistency using Ol-
lama
Added retry logic with exponential backoff and
validated vector dimensions
LLM response delays or timeouts Implemented timeout and fallback logic using
Axios and cache memory
Low chunk relevance in PDF answers Improved chunking strategy using overlap and
semantic boundaries
Empty chats being saved Added strict validation to only save non-empty
chats after user input
Slow UI transitions and modern expe-
rience
Used Framer Motion and optimized rendering via
conditional rendering and state management
PDF parsing errors (e.g., password-
protected files)
Validated and rejected unsupported files early, with
user-facing error messages
Table 4.1 Technical Challenges and Their Solutions
Each of these technical obstacles strengthened my practical debugging skills
and deepened my understanding of system behavior under edge-case scenarios.
36
4.3 Suggestions for Future Training Improvements
• Introduce Early Automated Testing: Automated test cases (unit +
integration) should be prioritized in the early development stages to reduce
debugging effort in later stages.
• Code Documentation Practices: Every project should maintain a proper
README, inline comments, and component-level documentation for easier
onboarding and collaboration.
• Real Deployment Experience: Training should include hands-on deployment
to platforms like Vercel, Render, DigitalOcean, or local server deployment.
This teaches CI/CD pipelines and production debugging.
• Include Basic DevOps Skills: Skills like monitoring resource usage,
analyzing logs, setting rate limits, or using PSM2 to manage backend apps
would be valuable for scalability.
4.4 Final Reflection
This training has been a transformative experience, allowing me to apply
classroom theories into a real-world full-stack application. I gained hands-on
experience in:
• Integrating LLMs with document processing
• Managing complex React state and animations
• Backend data flow with MongoDB, Express, and REST APIs
• Developing smart chat systems and UI/UX logic
It has boosted my technical confidence, problem-solving skills, and collab-
orative capabilities. I feel more prepared now to enter the professional software
engineering field with solid practical knowledge of AI system development.
37