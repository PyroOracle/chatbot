-- ================================
-- TechnoBot Chatbot Database Schema
-- Supports: Job Seeker & Client Forms
-- DBMS: PostgreSQL / MySQL Compatible
-- ================================

-- ============================
-- Table 1: Job Seekers
-- ============================
CREATE TABLE job_seekers (
    id SERIAL PRIMARY KEY,                           -- Auto-incrementing ID
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20),
    linkedin_url TEXT,
    social_media TEXT,
    experience_years INT CHECK (experience_years >= 0),
    preferred_department VARCHAR(100),
    resume_link TEXT,                                -- Optional: Link to uploaded CV
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================
-- Table 2: Clients
-- ============================
CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    company_name VARCHAR(150) NOT NULL,
    contact_person VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20),
    requested_service VARCHAR(100),
    project_description TEXT,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================
-- Optional Indexes (Optimization)
-- ============================
CREATE INDEX idx_job_seekers_email ON job_seekers(email);
CREATE INDEX idx_clients_email ON clients(email);
