from django.views.generic import TemplateView

from portfolio.models import Project


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["featured_projects"] = (
            Project.objects
            .filter(featured=True)
            .order_by("-created_at")[:3]
        )

        return context


class AboutView(TemplateView):
    template_name = "about.html"


class SkillsView(TemplateView):
    template_name = "core/skills.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["software_skills"] = [
            {
                "name": "Python",
                "description": "Programming, automation, backend development and data processing.",
                "level": "Advanced",
            },
            {
                "name": "Django",
                "description": "Building full-stack web applications and backend systems.",
                "level": "Advanced",
            },
            {
                "name": "FastAPI",
                "description": "Building modern, high-performance REST APIs.",
                "level": "Intermediate",
            },
            {
                "name": "Flutter",
                "description": "Building cross-platform mobile applications.",
                "level": "Intermediate",
            },
            {
                "name": "C#",
                "description": "Desktop applications, object-oriented programming and application development.",
                "level": "Intermediate",
            },
            {
                "name": "WPF / MVVM",
                "description": "Building structured Windows desktop applications using MVVM architecture.",
                "level": "Intermediate",
            },
            {
                "name": "SQL",
                "description": "Database design, querying, CRUD operations and data analysis.",
                "level": "Advanced",
            },
            {
                "name": "JavaScript",
                "description": "Frontend interactions and web application development.",
                "level": "Intermediate",
            },
        ]

        context["automation_skills"] = [
            {
                "name": "PLC Programming",
                "description": "Industrial control logic, sequencing and automation systems.",
            },
            {
                "name": "HMI",
                "description": "Human-machine interface development and operator visualization.",
            },
            {
                "name": "SCADA",
                "description": "Supervisory control, monitoring and industrial data visualization.",
            },
            {
                "name": "Instrumentation",
                "description": "Industrial measurement, control and process instrumentation.",
            },
            {
                "name": "Siemens",
                "description": "PLC programming and industrial automation using Siemens platforms.",
            },
            {
                "name": "Industrial Networks",
                "description": "Working with industrial communication and networking technologies.",
            },
        ]

        context["embedded_skills"] = [
            {
                "name": "STM32",
                "description": "Microcontroller programming and embedded systems development.",
            },
            {
                "name": "ESP32",
                "description": "Embedded applications, connectivity and IoT experimentation.",
            },
            {
                "name": "C/C++",
                "description": "Low-level programming and firmware development.",
            },
            {
                "name": "Electronics",
                "description": "Understanding hardware, sensors, signals and microcontroller interfaces.",
            },
        ]

        context["data_skills"] = [
            {
                "name": "Power BI",
                "description": "Interactive dashboards, reporting and business intelligence.",
            },
            {
                "name": "Data Analysis",
                "description": "Turning raw operational data into useful insights.",
            },
            {
                "name": "Excel",
                "description": "Data analysis, reporting and visualization.",
            },
            {
                "name": "Data Visualization",
                "description": "Presenting information clearly through meaningful visualizations.",
            },
        ]

        return context