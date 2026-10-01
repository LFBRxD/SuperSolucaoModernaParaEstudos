{{- define "notifications-service.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "notifications-service.fullname" -}}
{{- if .Values.fullnameOverride -}}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name (include "notifications-service.name" .) | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}

{{- define "notifications-service.labels" -}}
app.kubernetes.io/name: {{ include "notifications-service.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}

{{- define "notifications-service.selectorLabels" -}}
app.kubernetes.io/name: {{ include "notifications-service.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}
